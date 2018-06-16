"""
create temp-file
(needs to be called before you can run any action)
"""
import logging
import tempfile
import json
import os
from ifc_model.project import Project

def dump(ifc_file, filename=None):
    if not filename:
        tmp_fd, filename = tempfile.mkstemp(prefix='ifc_exchange_', suffix='.json')
        os.close(tmp_fd)
    logging.info('store json to: {}'.format(filename))
    project = Project()
    project.open_ifc(ifc_file)
    data = project.to_json()
    json.dump(
        project.to_json(),
        open(filename, 'w'),
        indent=2,
        sort_keys=True
    )
    return project, filename

def load_ifc(ifc_file, save=None, **kwargs):
    project, json_file = dump(ifc_file, save)
    if not save:
        os.remove(json_file)
    return project
