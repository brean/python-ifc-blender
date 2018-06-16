import bpy
import logging
import os

def run_import(project, ifc_file, **kwargs):
    if not os.path.exists(ifc_file):
        logging.error('file not found {}'.format(ifc_file))
    bpy.ops.import_scene.ifc(filepath=ifc_file)
