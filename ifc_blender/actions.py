'''
load actions from config files
'''
import os
import logging
import glob
import json
import logging
import bpy

from . import ifc_to_json
from . import cleanup
from . import blacklist
from . import group
from . import visibility
from . import io
from . import mesh
from . import replace
from . import exporter
from . import importer

actions = {
    'remove_site': cleanup.remove_site,
    'blacklist': blacklist.remove,
    'remove_hidden': cleanup.remove_hidden,
    'create_group': group.create,
    'show': visibility.show_hidden,
    'save': io.save,
    'load': io.load,
    'add_group': group.add,
    'create_group': group.create,
    'group_split': group.split,
    'group_children_by_regex': group.children_by_regex,
    'group_by_regex': group.by_regex,
    'group_by_elevation': group.by_elevation,
    'replace': replace.replace,
    'export': exporter.export,
    'import': importer.run_import,
    'load_ifc': ifc_to_json.load_ifc,
    'group_unlink': group.unlink,
    'mesh_split': mesh.split,
    'mesh_remove': mesh.remove,
    'mesh_reposition': mesh.reposition
}


def execute_action(data, project):
    name = data['name']
    if not name in actions:
        logging.warn('can not find action {}'.format(name))
        return

    description = ': {}'.format(data['description']) if 'description' in data else ''
    logging.info('execute action {}{}'.format(name, description))

    data['project'] = project
    return actions[name](**data)


def load(path):
    project = None
    for filename in glob.glob(os.path.join(path, '*.json')):
        logging.info('loading {}'.format(filename))
        with open(filename) as json_file:
            for action in json.load(json_file):
                p = execute_action(action, project)
                if p:
                    project = p
