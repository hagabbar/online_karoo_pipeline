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
     GPS_obj = data.get_peak().astype(float)
     gps_array = []
     q_array = []
     print 'processing triggers'

#     for idx in range(0,len(GPS_obj)):
#         time = data.get_peak()[idx].gpsSeconds
#         gps_array.append(time)

     SNR = data.get_z()
     mask = SNR > 7.5
     trig_times = np.asarray(GPS_obj)[mask]
     del gps_array
     #q = data.get_q()[mask]
     #bw = data.get_column('bandwidth')[mask]
     #dur = data.get_column('duration')[mask]
     #freq = data.get_column('peak_frequency')[mask]

     return GPS_obj  #, q, mask, bw, dur, freq, data

#def karoo_pip():
    

if __name__ == '__main__':
    #construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-ifo", "--observatory", required=False,
            help="observatory")
    ap.add_argument("-s", "--start_time", required=True,
            help="start time")
    ap.add_argument("-e", "--end_time", required=True,
            help="end time")
    args = vars(ap.parse_args())

    #Initializing parameters
    ifo = args['observatory']
    st = int(args['start_time'])
    et = int(args['end_time'])

    #Extract trig files
    cache = locate_trigs(ifo,st,et)
    
    #Perform pre-processing of triggers (snr > 7.5)
    trigs = preproc(cache)    
   
    np.save('luciano_h1trigs.npy', trigs)
    #Run script for generating features
    #Need location for script and parameters to feed into it. Ask Marco?

    #Process features against karoo generated multivariant expression, one for each type of glitch


    #Write in an html page if gltich type of not
 
