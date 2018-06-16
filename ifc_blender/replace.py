import logging
import bpy
from . import bpy_helper
from .ifc_helper import elements_by_type
from .blacklist import blacklisted

'''
append object from other blender file
'''
def append_object(blend_file, object_name, section='/Object/'):
    blend_file = blend_file + '.blend'
    filepath  = blend_file + section + object_name
    directory = blend_file + section
    filename  = object_name

    state = bpy.ops.wm.append(
        filepath=filepath,
        filename=filename,
        directory=directory)

    obj = bpy.data.objects.get(object_name)
    return obj

'''
replace object with another object in blender (after append)
and get its name/data
'''
def replace_object(obj, other, copy_dimensions=False):
    logging.warn('replace {} with {}'.format(obj.name, other.name))
    other.location = obj.location
    if copy_dimensions:
        other.dimensions = obj.dimensions
    name = obj.name
    mesh_name = obj.data.name
    obj.name = 'del_'+obj.name
    obj.data.name = 'del_'+obj.data.name
    bpy.data.objects.remove(obj, True)
    other.name = name
    other.data.name = mesh_name

def replace(project, blend_file, object_name, ifc_type, regex=None, copy_dimensions=False, **kwargs):
    products = elements_by_type(project, 'product')
    for product in products:
        obj = bpy_helper.find_object(product)
        if not obj:
            # logging.warn('can not find ' + product.name)
            # product not in blend-file... (ignored)
            continue
        if blacklisted(obj, ifc_type, regex):
            other_obj = append_object(blend_file, object_name)
            replace_object(obj, other_obj, copy_dimensions)
