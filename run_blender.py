# -*- coding: UTF-8 -*-
# parse ifc file, create structure and store it into json file
# please install/copy ifcopenshell-python for 3.5 and python-model to
# C:\Program Files\Blender Foundation\Blender\2.78\python\lib\site-packages first

import logging
import sys
import os
import glob
path = os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, path)

from ifc_blender.actions import load
#import ifcopenshell
#from ifc_model.project import Project


def log_setup():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('IFC;%(name)s;%(levelname)s;%(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

def main():
    #log_setup()
    load('actions/')

main()
