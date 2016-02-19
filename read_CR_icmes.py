# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:23:13 2016

@author: alysha.reinard
"""
import numpy as np
from datetime import datetime
import pickle
from numpy.lib import recfunctions as rfn

def with_indexing(dstr):
    return datetime(*map(int, [dstr[:4], dstr[5:7], dstr[8:10], dstr[11:13], dstr[13:15]])) 
 
def main():
#    names=['year', 'Disturbance', 'ICME', 'Composition', 'MCstartend', 'BDE', 'BIF', \
#    'Qual.', 'dV', 'V_ICME',	'V_max', 'Bfield', 'MC', 'Dst', 'V_transit', \
#    'LASCO_CME']

#    with open("icmetable2.csv", "rt") as f:    
#        reader=csv.reader(f, delimiter=',')
#        names=reader.__next__()

    CRicmes=np.genfromtxt("icmetable2.csv", delimiter=',', names=True, dtype=None)
    
    year=CRicmes['year']
    dist=CRicmes['Disturbance']
    ICMEstart=CRicmes['ICMEstart']
    ICMEend=CRicmes['ICMEend']
    LASCO_CME=CRicmes['LASCO_CME']

#    print(type(dist))
#    print(type(dist[0]))
#    print(dist)
#    print(type(dist))
#    print(CRicmes['LASCO_CME'])
    Disturbance_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, dist)]
    Disturbance_time=np.array([datetime.strptime(Disturbance_wyear[i], "%Y %m/%d %H%M") for i in range(len(Disturbance_wyear))])

    ICMEstart_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, ICMEstart)]
    ICMEstart_time=np.array([datetime.strptime(ICMEstart_wyear[i], "%Y %m/%d %H%M") for i in range(len(ICMEstart))])

    ICMEend_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, ICMEend)]
    ICMEend_time=np.array([datetime.strptime(ICMEend_wyear[i], "%Y %m/%d %H%M") for i in range(len(ICMEend))])

    LASCO_CME_time=[]
    for (x,y) in zip(year, LASCO_CME):
#        if y != b'' and y!=b'...':
        try:
#            print("y: ", y)
            temp=str(x)+" "+y.decode('UTF-8')[0:10]
            LASCO_CME_time.append(datetime.strptime(temp, "%Y %m/%d %H%M"))

        except:
            LASCO_CME_time.append("")
    LASCO_CME_time=np.array(LASCO_CME_time)
 
#    CRicmes['Disturbance']=Disturbance_time
#    CRicmes['ICMEstart']=ICMEstart_time
#    CRicmes['ICMEend']=ICMEend_time
#    CRicmes['LASCO_CME']=LASCO_CME_time#, dtype=datetime6
    print(len(CRicmes))      
    np.reshape(CRicmes["Compstart"], len(CRicmes))
    print(CRicmes["Compstart"].shape)
    print(len(LASCO_CME_time))
    CRicmes_wdatetime=np.vstack((CRicmes["Compstart"], CRicmes["Compend"], Disturbance_time, ICMEstart_time, ICMEend_time, LASCO_CME_time))
    #CRicmes_wdatetime=[CRicmes.tolist(), Disturbance_time, ICMEstart_time, ICMEend_time, LASCO_CME_time]
#    rfn.merge_arrays(CRicmes_wdatetime, flatten=True, usemask=False)
#    rfn.append_fields(CRicmes, names=["Disturbance_date", 
#    "ICMEstart_date", "ICMEend_date", "LASCO_date"], data=[Disturbance_time, 
#    ICMEstart_time, ICMEend_time, LASCO_CME_time], usemask=False)

     
#    print(CRicmes['LASCO_CME'])
#    print(CRicmes)
    print(CRicmes_wdatetime.shape)
    print(type(CRicmes_wdatetime))
        #TODO figure out how to concatenate arrays http://stackoverflow.com/questions/18574132/python-numpy-concatenation-of-named-arrays
    
    
    
    filehandler=open('CR_icmes.p', 'wb')
    pickle.dump(CRicmes_wdatetime, filehandler)
    
    
main()