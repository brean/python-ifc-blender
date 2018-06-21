# IFC-Blender
import and manipulate an IFC in Blender based on IFCOpenShell

A workflow could look like this:
1. You create some building in Revit (or get it from an architect).
1. You export your Model to IFC
1. You use this script to import the model to Blender and do something with it (e.g. split by level to and export to FBX, so you have multiple files for each storey). Also a small JSON-file will be generated storing infromation from the IFC (like storeys, rooms, ... - using [Python-IFC-Model](https://github.com/brean/python-ifc-model).
1. You use the FBX in a 3D-Engine like Unity to display the building. You can then add some logic to animate the level.
1. If you like to show specific data or find single elements from the IFC in your app you can simply

# Installation
## Install Blender IFC Add-On
1. Install Blender using the graphical installer from [the Blender download page](https://www.blender.org/download/)
1. Download IFCOpenShell from [The IFCOpenShell download page](http://ifcopenshell.org/)
   Make sure you have the right version. For your Blender Version, the 0.5.0 preview 2 works fine with Blender 2.78. ![IFCOpenShell for Blender](docs/images/blender_install_ifc.PNG?raw=true)
1. Start Blender and press CTRL-ALT-U to open the User Settings
1. click on "Add-ons" and then the "Install Add-on from File..." button
   ![install addon](docs/images/blender_install_addon.png?raw=true).
1. Select the downloaded IfcOpenShell-zip file and import it.
1. Now the Import-Export IfcBlender-Add-On should be available. If you search for "ifc" you should see it. Activate it by clicking on the checkbox to the left of its entry:
   ![activate addon](docs/images/blender_activate_addon.png?raw=true).
1. (optional) if you like to load the Add-on every time Blender starts click the "Save User Settings"-button.
1. Close the "User Preferences" window and make sure the installation was successful. Under "File" -> "Import" you should see "Industry Foundation Classes (.ifc)"<br/>
   ![IFC in Blender](docs/images/blender_start_ifc_addon.png?raw=true).
1. Quit Blender

## Install IfcBlender
1. Download/Checkout [ifc_model](https://github.com/brean/python-ifc-model)
1. Extract the downloaded IfcOpenShell package and copy the folder content as well as the ifc_model folder from python-ifc-model to `<Blender Installation Folder>\<Blender Version>\python\lib`
   ![Python-libs inside Blender](docs/images/ifc_model_path.png?raw=true)

(TODO: installing this as Blender Add-On from the UI would be nice...)

# Export from Revit
It is the easiest when we export the 3D-representation of spaces (space boundaries), so we can use them as objects in Blender.

When you like to import your Revit model you should select "1st level" in Revit when exporting:

![IFC-Export with 1st level selected](docs/images/ifc_export_revit_1st_level.png?raw=true)

# Running the example
There is an example json-file that creates separated .blend files for all storeys, based on the ["FZK Haus" from the IFC Wiki](http://www.ifcwiki.org/index.php?title=KIT_IFC_Examples)
Just download this file, save it to the buildings/-folder and execute "run.bat".

# JSON configuration
What happens in Blender to the imported IFC can be configured in a JSON-file. When executing "run_blender.py" (e.g. by executing "run.bat") it will iterate over all files in actions/ and load all JSON-files saved there.

Possible JSON-Attributes can be:

|JSON|description|
|---|---|
|"name": "**load_ifc**",<br/> "save": "out/AC20-FZK-Haus.json",<br/> "ifc_file": "buildings/AC20-FZK-Haus.ifc"|loads an *ifc_file* and create its JSON-representation in the *save* location|
|"name": **"mesh_remove"**, <br/>"mesh_name": "Cube"|Blender helper-function to remove the mesh with *mesh_name*. Useful to remove the starting cube|
|"name": **"import"**, <br/>"ifc_file": "buildings/AC20-FZK-Haus.ifc"|Imports an IFC-file into blender using IfcOpenShell|
|"name": "**load**",<br/>"filepath": "buildings/AC20-FZK-Haus.blend"|load a .blend file that has been imported using IfcOpenShell (useful when the import takes long and you like to import manually on another machine)|
|"name": **"show"**,<br/>"ifc_type": "space"|sets all objects with the given IFC-type to visible (in this case all IfcSpaces)|
|"name": **"remove_site"**|removes the mesh for the IfcSite|
|"name": **"blacklist"**,<br/>"ifc_type": "IfcBuildingElementProxy",<br/>"regex": "ABZUGSK.*"|removes all objects of type *ifc_type* ("IfcBuildingElementProxy") with the name matching the *regex* (everything starting with "ABZUGSK")|
|"name": **"remove_hidden"**|removes all invisible/disabled elements (you might to use this after "show")|
|"name": **"replace"**,<br/> "copy_dimensions": false,<br/>,"regex": "Chair.*",<br/> "blend_file": "lowpoly/simple_chair,<br/> "ifc_type": "IfcFurnishingElement",<br/>"object_name": "chair"|replaces every object with the type *ifc_type* that matches the given regex (starts with *Chair*) with the object *object_name* (chair) from the Blender file *blend_file*. Useful to replace elements from the IFC file with other elements that have a lower or higher level of detail. Either to enhance for VR-Environments or to lower the poly count on mobile devices|
|"name": **"create_group"**,<br/> "ifc_type": "storey"|creates a new group based on the *ifc_type*. Useful to create groups that can be exported later on in single .blend files and exported as single FBX/OBJ|
|"name": **"add_group"**,<br/> "ifc_type_group": "storey",<br/>"ifc_children":"spaces"|add aditional objects to a group that has been created with *add_group*. In this example all spaces of a storey will also be added to their storey-group|
|"name": **"group_children_by_regex"**,<br/>    "ifc_target_groups": "storey",<br/>"target_regex": ".* (?P<name>-?[0-9]\\d*)",<br/>"source_regex": ".*\\.(?P<name>-?[0-9]\\d*)\\..*",|add all elements of the group that matches the *source_regex* to the *ifc_target_group* type matching the *target_regex* regex|
|"name": **"group_unlink"**,<br/> "regex": "*^GROUP.*"|removes all objects from a group where the name mathes the *regex*|
|"name": **"mesh_reposition"**,<br/> "regex": "*^GROUP.*"|recalculate the vertice center position of all objects matching the group name. Useful in combination with *group_by_elevation*|
|"name": **"group_by_elevation"**|add all elements to the group for their story. (reads story-height from IFC)|
|"name": **"mesh_split"**,<br/> "regex": "*^LOGO.*"<br/>"split_z": 1.2|cuts the object in two objects, after given *split_z* value (in meters)|
|"name": **"export"**,<br/> "filepath": "out/House"<br/>"filetype": ["obj", "fbx"]|export the building (in this case as fbx which works quite well in Unity3D and obj which is great for WebGL/THREE.js)|
|"name": **"save"**,<br/> "filepath": "out/House"|save as .blend file|
|"name": **"group_split"**,<br/>"ifc_type": "storey",<br/>"outpath": "out",<br/>"blend_file": "out/House",<br/>"export": ["obj", "fbx"]|loads the given blend-file for every entry in the "ifc_type" (e.g. each storey) delete everything else and export it. Useful to get single files for each storey. **WARNING** because this needs to load the .blend-file make sure you save the building with *save* and do this as the last step!|
