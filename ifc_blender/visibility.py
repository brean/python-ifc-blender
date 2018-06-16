import bpy
import logging
from . import bpy_helper
from . import ifc_helper

"""
show all elements by given IFC-type
"""
def show_hidden(project, ifc_type, **kwargs):
    ifc_elems = ifc_helper.elements_by_type(project, ifc_type)
    ifc_names = [elem.name for elem in ifc_elems]
    i = 0
    for obj in bpy.data.objects:
        if obj.hide and obj.name in ifc_names:
            i += 1
            # logging.info('{}: show {}'.format(i, obj.name))
            obj.hide = False
    logging.info('show {} hidden objects'.format(i))
