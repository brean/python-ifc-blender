import os
import re
import bpy
import logging
import json
from . import bpy_helper
from . import ifc_helper
from . import io
from . import exporter

def create(project, ifc_type=None, group_name='', prefix='', **kwargs):
    i = 0

    if ifc_type:
        for elem in ifc_helper.elements_by_type(project, ifc_type):
            i += 1
            grp_name = prefix + elem.name
            logging.info('{}: create group {}'.format(i, grp_name))
            grp = bpy.data.groups.new(grp_name)
    else:
        grp_name = prefix + group_name
        logging.info('{}: create group {}'.format(i, grp_name))
        grp = bpy.data.groups.new(grp_name)

def children_by_regex(project, ifc_target_groups, source_regex, target_regex,
        force_int=False, source_prefix='', prefix='', **kwargs):
    i = 0
    # get all storeys
    target_names = {}
    for group in ifc_helper.elements_by_type(project, ifc_target_groups):
        m = re.match(target_regex, group.name)
        if m:
            name = m.group('name')
            if force_int:
                name = int(name)
            target_names[name] = prefix+group.name

    # find blender groups that are not assigned to the target
    for source_group in bpy.data.groups:
        source_name = source_group.name
        m = re.match(source_regex, source_name)
        if m:
            group_nr = m.group('name')
            if force_int:
                group_nr = int(group_nr)
            target_name = target_names[group_nr]
            logging.info('assign all elements of group {} to {}'.format(
                source_name, target_name
            ))
            for obj in bpy.data.groups[source_name].objects:
                if not obj.name in bpy.data.groups[target_name].objects:
                    bpy.data.groups[target_name].objects.link(obj)
                    i += 1
                    #logging.info('assign {} to {}'.format(
                    #    obj.name, target_name
                    #))
            logging.info("assigned {} objects to group {}".format(i, target_name))


def _by_elevation(building, prefix=''):
    min_elevation = -20
    max_elevation = 1000
    elevations = {}
    for storey in building.storeys:
        elevations[storey.name] = [storey.elevation, 0]
    # calculate min and max for elevation
    ele = [e[0] for e in elevations.values()] + [max_elevation]
    for elevation in elevations.values():
        elevation[1] = min([e for e in ele if e > elevation[0]])
    min([x for x in elevations.values()])[0] = min_elevation
    logging.info("elevations: " + json.dumps(elevations, indent=2))
    i = 0
    for obj in bpy.data.objects:
        num_groups = sum([obj.name in g.objects for g in bpy.data.groups])
        if num_groups == 0:
            if not obj.data.vertices:
                continue
            vcos = [ obj.matrix_world * v.co for v in obj.data.vertices ]
            findCenter = lambda l: ( max(l) + min(l) ) / 2

            x,y,z  = [ [ v[i] for v in vcos ] for i in range(3) ]
            center = [ findCenter(axis) for axis in [x,y,z] ]
        
            z = center[2]
            grp_name = [n for n, e in elevations.items() if e[0] <= z < e[1]]
            if grp_name:
                grp_name = prefix + grp_name[0]
                # logging.info('assign {} to {} - {}'.format(
                #    obj.name, grp_name, z
                # ))
                bpy.data.groups[grp_name].objects.link(obj)
                i += 1
    logging.info("assigned {} objects to group by elevation".format(i))



def by_elevation(project, prefix='', **kwargs):
    for site in project.sites:
        for building in site.buildings:
            _by_elevation(building, prefix)


def by_regex(project, ifc_type_group, group_name, regex, **kwargs):
    i = 0
    for elem in ifc_helper.elements_by_type(project, ifc_type_group):
        m = re.search(regex, elem.name)
        if not m:
            continue
        obj = bpy_helper.find_object(elem)
        print(obj)
        print(elem.name)
        if not obj.name in bpy.data.groups[group_name].objects:
            bpy.data.groups[group_name].objects.link(obj)
            i += 1
            #logging.info('assign {} to {}'.format(
            #    obj.name, group_name
            #))
    logging.info("assigned {} objects to group {}".format(i, group_name))


def unlink(project, regex, **kwargs):
    i = 0
    for obj in bpy.data.objects:
        m = re.match(regex, obj.name)
        if not m:
            continue
        for grp in obj.users_group:
            grp.objects.unlink(obj)
            i += 1
    logging.info("unlinked {} objects from groups, {} '{}'".format(i, len(bpy.data.objects), regex))


def add(project, ifc_type_group, prefix='', ifc_children=None, **kwargs):
    # get group
    for group in ifc_helper.elements_by_type(project, ifc_type_group):
        i = 0
        j = 0
        grp_name = prefix + group.name
        # assign self to group
        if not ifc_children:
            continue
        # assign item to group
        for elem in getattr(group, ifc_children):
            i += 1
            obj = bpy_helper.find_object(elem)
            if not obj:
                # logging.error('can not assign {} to group {}'.format(elem.name, grp_name))
                j += 1
                continue
            if obj.name in bpy.data.groups[grp_name].objects:
                logging.warn('DUPLICATE: object {} already in group {}'.format(elem.name, grp_name))
                continue
            # logging.info('{}: link {} to group {}'.format(i, elem.name, grp_name))
            bpy.data.groups[grp_name].objects.link(obj)
        logging.info("linked {} objects to group {}".format(i, grp_name))
        if j:
            logging.warn("could not assign {} objects to group {}".format(j, grp_name))
    # get all products
    #for elem in ifc_helper.elements_by_type(project, ifc_type_group):
    #    # find out which room/storey they are assigned to

    #for item in ifc_helper.elements_by_type(project, ifc_type):
    #    ifc_helper.elements_by_type(project, 'product')


"""
split into multiple .blend-files based on blender groups and ifc_type
"""
def split(project, ifc_type, outpath, blend_file, export=None, **kwargs):
    
    elements = ifc_helper.elements_by_type(project, ifc_type)
    for elem in elements:
        i = 0
        io.load(blend_file)
        logging.info('delete all but {}'.format(elem.name))
        for other in elements:
            if other == elem:
                continue
            # remove all other groups
            for obj in bpy.data.groups[other.name].objects:
                # logging.info('delete {} from group {}'.format(obj.name, other.name))
                i += 1
                bpy.data.objects.remove(obj, True)
        logging.info('delete {} objects from group {}, kept {}'.format(i, elem.name, len(bpy.data.objects)))
        filepath = os.path.join(outpath, elem.name)
        io.save(filepath)
        if export:
            exporter.export(project, filepath, export)
