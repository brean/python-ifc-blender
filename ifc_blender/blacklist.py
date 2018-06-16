import bpy
import re
import logging
from . import bpy_helper
from .ifc_helper import elements_by_type

'''
check if this element matches the given ifc_type and regex
use empty ifc_type to get all elements
'''
def blacklisted(obj, ifc_type=None, regex=None):
    if ifc_type and obj.ifc_type != ifc_type:
        return False
    return not regex or re.match(regex, obj.name) != None


def remove(project, ifc_type=None, regex=None, **kwargs):
    i = 0
    objects = []
    if ifc_type:
        products = elements_by_type(project, 'product')
        for product in products:
            obj = bpy_helper.find_object(product)
            if obj:
                objects.append(obj)
            #else:
            # logging.warn('can not find ' + product.name)
            # product not in blend-file... (ignored)

    else:
        objects = bpy.data.objects

    for obj in objects:
        if blacklisted(obj, ifc_type, regex):
            i += 1
            # logging.warn('{}: remove blacklisted: {}'.format(i, obj.name))
            bpy.data.objects.remove(obj, True)
    logging.info("removed {} blacklisted objects".format(i))
