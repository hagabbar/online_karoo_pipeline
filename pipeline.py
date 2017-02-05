#Author: Hunter Gabbard
#Max Planck Institute for Gravitational Physics
#Need to source Duncan's gwpy environ prior to running script (source ~detchar/opt/gwpysoft/bin/activate)

import sys
import os
import numpy as np
import argparse
from trigfind import find_trigger_files


def locate_trigs(st,et):
    urls = trigfind.find_trigger_files('L1:GDS-CALIB_STRAIN', 'Omicron', st, et)

    return urls

if __name__ == '__main__':
    #construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--start-time", required=True,
            help="start time")
    ap.add_argument("-e", "--end-time", required=True,
            help="end time")

    #Extract trig files
    files = locate_trigs(st,et)
    
    #Perform pre-processing of triggers (snr > 7.5)
    
