# IFC-Blender
import and manipulate an IFC in Blender based on IFCOpenShell

# Installation
1. Install Blender using the graphical installer from [the Blender download page](https://www.blender.org/download/)
1. Download IFCOpenShell from [The IFCOpenShell download page](http://ifcopenshell.org/)
   Make sure you have the right version. For your Blender Version, the 0.5.0 preview 2 works fine with Blender 2.78. ![IFCOpenShell for Blender](docs/images/blender_install_ifc.png?raw=true)
1. download/checkout [ifc_model](https://github.com/brean/python-ifc-model)
1. Extract the downloaded IfcOpenShell package and copy the folder content as well as the ifc_model folder from python-ifc-model to `<Blender Installation Folder>\<Blender Version>\python\lib`
   ![Python-libs inside Blender](docs/images/ifc_model_path.png?raw=true)
1. Start Blender and click on "File"->"User Preferences".
1. In the "Blender User Preferences" Window click on Install Add-on from File

# Export from Revit
It is is the easiest when we export the 3D-representation of spaces, so we can use them as objects in Blender.

When you like to import your Revit model you should select "1st level" in Revit when exporting:

![IFC-Export with 1st level selected](docs/images/ifc_export_revit_1st_level.png?raw=true)

# Running the example
there is an example json-file that creates separated .blend files for all stories, based on the [FZK Haus from the IFC Wiki](http://www.ifcwiki.org/index.php?title=KIT_IFC_Examples)
