import bpy
import logging
from . import io

# string checking for python 2 and 3
try:
    isinstance("", basestring)
    def isstr(s):
        return isinstance(s, basestring)
except NameError:
    def isstr(s):
        return isinstance(s, str)

def export(project, filepath, filetype, **kwargs):
    if isstr(filetype):
        filetype = [filetype]
    for exp_type in filetype:
        _path = filepath
        if not _path.endswith('.'+exp_type):
            _path += '.'+exp_type
        if exp_type == 'obj':
            logging.info('export as obj to {}'.format(_path))
            bpy.ops.export_scene.obj(filepath=_path)
        elif exp_type == 'fbx':
            logging.info('export as fbx to {}'.format(_path))
            bpy.ops.export_scene.fbx(filepath=_path)
