"""
save blend file
"""
import logging
import bpy

def save(filepath, **kwargs):
    logging.info('save as {}'.format(filepath))
    bpy.ops.wm.save_as_mainfile(filepath=filepath + '.blend')

def load(filepath, **kwargs):
    logging.info('load {}'.format(filepath))
    bpy.ops.wm.open_mainfile(filepath=filepath + '.blend')
