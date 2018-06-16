import bpy
import logging
from . import bpy_helper

'''
remove not selected objects
'''
def remove_hidden(project, **kwargs):
    i = 0
    for obj in bpy.data.objects:
        if obj.hide:
            i+=1
            # logging.warn('{}: remove invisible: {}'.format(i, obj.name))
            bpy.data.objects.remove(obj, True)
    logging.info("removed {} invisible objects".format(i))

'''
remove other sites, we just want the building
'''
def remove_site(project, **kwargs):
    i = 0
    for site in project.sites:
        obj = bpy_helper.find_object(site)
        if obj:
            i += 1
            logging.warn('{}: remove site: {}'.format(i, obj.name))
            bpy.data.objects.remove(obj, True)
