# IFC-Blender
import and manipulate an IFC in Blender based on IFCOpenShell

A workflow could look like this:
1. You create some building in Revit (or get it from an architect).
1. You export your Model to IFC
1. You use IFC-Blender to import the model to Blender and do something with it (e.g. split by storey and export to FBX, so you have multiple files for each storey). See [actions.md](https://github.com/brean/ifc_blender/blob/master/docs/actions.md) for a list of all possible actions that you can use to manipulate the imported IFC in Blender. Also a small JSON-file will be generated storing infromation from the IFC (like storeys, rooms, ... - using [Python-IFC-Model](https://github.com/brean/python-ifc-model).
1. You use the FBX in a 3D-Engine like Unity to display the building. You can then add some logic to animate the building or just show it in VR/AR.
1. If you like to show specific data from the IFC or find single elements to highlight in your app you can simply load the JSON file and map the names of the objects in the fbx/obj with the data from the JSON-file.

You can also combine this with other blender functionality, e.g. to animate single IFC types (like storeys):

![Storey animation](docs/animations/storey_animation.gif?raw=true)

Or use it in the browser, for example using [https://threejs.org/](three.js) to figure out which room an element is placed at. (In this web application for example we use the IfcSpace information from the JSON file to detect in which room our air condition is dragged - see room number in the up-right corner when the object is moved).

![Object movement, space detection](docs/animations/room_detect.gif?raw=true)

# Installation
see [install](docs/install.md)

# Export from Autodesk Revit
see [revit](docs/revit.md)

# Running the example
There is an example json-file that creates separated .blend files for all storeys, based on the ["FZK Haus" from the IFC Wiki](http://www.ifcwiki.org/index.php?title=KIT_IFC_Examples)
Just download this file, save it to the buildings/-folder and execute "run.bat".

# JSON configuration
What happens in Blender to the imported IFC can be configured in a JSON-file. When executing "run_blender.py" (e.g. by executing "run.bat") it will iterate over all files in actions/ and load all JSON-files saved there.

An overview of all possible actions can be seen in [actions.md](docs/actions.md)
