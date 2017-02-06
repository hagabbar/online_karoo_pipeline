#Author: Hunter Gabbard
#Max Planck Institute for Gravitational Physics
#Need to source Duncan's gwpy environ prior to running script (source ~detchar/opt/gwpysoft/bin/activate)

import sys
import os
import numpy as np
import argparse
import trigfind
from trigfind import find_trigger_files
from gwpy.timeseries import TimeSeries
from gwpy.table.lsctables import SnglBurstTable

def locate_trigs(ifo,st,et):
    cache = trigfind.find_trigger_files('%s:GDS-CALIB_STRAIN' % ifo, 'Omicron', st, et)

    return cache

def preproc(cache):
     data = SnglBurstTable.read(cache)
     GPS_obj = data.get_peak()
     gps_array = []
     for idx in range(0,len(GPS_obj)):
         time = data.get_peak()[idx].gpsSeconds
         gps_array.append(time)
     SNR = data.get_z()
     mask = SNR > 7.5
     trigs = np.asarray(gps_array)[mask]

     return trigs

def karoo_pip():
    

if __name__ == '__main__':
    #construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-ifo", "--observatory", required=True,
            help="observatory")
    ap.add_argument("-s", "--start-time", required=True,
            help="start time")
    ap.add_argument("-e", "--end-time", required=True,
            help="end time")
    args = vars(ap.parse_args())

    #Initializing parameters
    ifo = args['ifo']
    st = args['st']
    et = args['et']

    #Extract trig files
    cache = locate_trigs(ifo,st,et)
    
    #Perform pre-processing of triggers (snr > 7.5)
    trigs = preproc(cache)    

    #Run script for generating features
    #Need location for script and parameters to feed into it. Ask Marco?

    #Process features against karoo generated multivariant expression, one for each type of glitch


    #Write in an html page if gltich type of not
 
