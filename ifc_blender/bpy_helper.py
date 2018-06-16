import bpy
import re

'''
find blender object (by name or mesh id)
'''
def find_object(product):
    blend_prod = bpy.data.objects.get(product.name)
    if blend_prod:
        return blend_prod

    # can not find the product by id
    # (probably because it is longer than 64 chars, try the mesh name)
    if hasattr(product, 'representations'):
        for obj in bpy.data.objects:
            if obj.type != 'MESH':
                continue
            for rep in product.representations:
                if obj.data.name == 'mesh'+str(rep.id):
                    return obj

    # last option - maybe this is an "umlaut-fail"
    for obj in bpy.data.objects:
        m = re.match('.*\:(?P<name>\d{3,9})[\:\d]*$', obj.name)
        if not m:
            continue
        name = m.group('name')
        if product.name.endswith(':{}'.format(name)):
            assert not product.name+'.001' in bpy.data.objects
            return obj
