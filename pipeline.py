#Author: Hunter Gabbard
#Max Planck Institute for Gravitational Physics
#Need to source Duncan's gwpy environ prior to running script (source ~detchar/opt/gwpysoft/bin/activate)

import sys
import os
import numpy as np
import argparse
from trigfind import find_trigger_files


def locate_trigs():
    trigfind.find_trigger_files('L1:GDS-CALIB_STRAIN', 'Omicron', 1135641617, 1135728017)

if __name__ == '__main__':
    #construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
