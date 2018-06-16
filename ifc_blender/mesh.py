import re
import bpy
import bmesh
import logging
from mathutils import Vector

"""
split mesh into different objects
"""
def split(regex, split_z, **kwargs):
    for obj in bpy.data.objects:
        m = re.match(regex, obj.name)
        if not m:
            continue
        for ob in bpy.data.objects:
            ob.select = False
        bpy.context.scene.objects.active = obj
        bpy.ops.object.mode_set(mode='EDIT')
        dmesh = obj.data
        mesh = bmesh.from_edit_mesh(dmesh)
        for f in mesh.faces:
            f.select = f.calc_center_median().z > split_z
        bpy.ops.mesh.separate(type='SELECTED')
        bmesh.update_edit_mesh(dmesh)
        dmesh.update()
        bpy.ops.object.mode_set(mode='OBJECT')

"""
remove mesh (e.g. starting cube)
"""
def remove(mesh_name, **kwargs):
    for ob in bpy.context.scene.objects:
        ob.select = ob.type == 'MESH' and ob.name.startswith(mesh_name)
    bpy.ops.object.delete()

"""
reposition by median
"""
def reposition(regex, **kwargs):
    for obj in bpy.data.objects:
        m = re.match(regex, obj.name)
        if not m:
            continue
        me = obj.data
        verts = [v.co for v in me.vertices]
        pivot = sum(verts, Vector()) / len(verts)
        for v in me.vertices:
            v.co.z -= pivot.z
        obj.location.z = pivot.z
