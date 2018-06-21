JSON-configuration

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
