#Author: Hunter Gabbard
#Max Planck Institute for Gravitational Physics
#Need to source Duncan's gwpy environ prior to running script (source ~detchar/opt/gwpysoft/bin/activate)

import sys
import os
import numpy as np
import argparse
from trigfind import find_trigger_files
from gwpy.timeseries import TimeSeries


def locate_trigs(st,et):
    cache = trigfind.find_trigger_files('L1:GDS-CALIB_STRAIN', 'Omicron', st, et)

    return cache

def preproc(cache):
     data = TimeSeries.read(cache, ‘L1:GDS-CALIB_STRAIN’)


if __name__ == '__main__':
    #construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--start-time", required=True,
            help="start time")
    ap.add_argument("-e", "--end-time", required=True,
            help="end time")

    #Extract trig files
    cache = locate_trigs(st,et)
    
    #Perform pre-processing of triggers (snr > 7.5)
    trigs = preproc(cache)    

    #Run script for generating features

    #Process features against karoo generated multivariant expression, one for each type of glitch

    #Write in an html page if gltich type of not
 
