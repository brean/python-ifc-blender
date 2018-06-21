# IFC-Blender
import and manipulate an IFC in Blender based on IFCOpenShell

A workflow could look like this:
1. You create some building in Revit (or get it from an architect).
1. You export your Model to IFC
1. You use this script to import the model to Blender and do something with it (e.g. split by level to and export to FBX, so you have multiple files for each storey). Also a small JSON-file will be generated storing infromation from the IFC (like storeys, rooms, ... - using [Python-IFC-Model](https://github.com/brean/python-ifc-model).
1. You use the FBX in a 3D-Engine like Unity to display the building. You can then add some logic to animate the level.
1. If you like to show specific data or find single elements from the IFC in your app you can simply

# Installation
see [install](docs/install.md)

# Export from Revit
It is the easiest when we export the 3D-representation of spaces (space boundaries), so we can use them as objects in Blender.

When you like to import your Revit model you should select "1st level" in Revit when exporting:

![IFC-Export with 1st level selected](docs/images/ifc_export_revit_1st_level.png?raw=true)

# Running the example
There is an example json-file that creates separated .blend files for all storeys, based on the ["FZK Haus" from the IFC Wiki](http://www.ifcwiki.org/index.php?title=KIT_IFC_Examples)
Just download this file, save it to the buildings/-folder and execute "run.bat".

# JSON configuration
What happens in Blender to the imported IFC can be configured in a JSON-file. When executing "run_blender.py" (e.g. by executing "run.bat") it will iterate over all files in actions/ and load all JSON-files saved there.

An overview of all possible actions can be seen in [actions.md](docs/actions.md)
