# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:23:13 2016

@author: alysha.reinard
"""
import csv
import numpy as np
from datetime import datetime

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
    print(CRicmes['LASCO_CME'])
    Disturbance_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, dist)]
    Disturbance_time=[datetime.strptime(Disturbance_wyear[i], "%Y %m/%d %H%M") for i in range(len(Disturbance_wyear))]

    ICMEstart_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, ICMEstart)]
    ICMEstart_time=[datetime.strptime(ICMEstart_wyear[i], "%Y %m/%d %H%M") for i in range(len(ICMEstart))]

    ICMEend_wyear=[str(x)+" "+y.decode('UTF-8')[0:10] for (x, y) in zip(year, ICMEend)]
    ICMEend_time=[datetime.strptime(ICMEend_wyear[i], "%Y %m/%d %H%M") for i in range(len(ICMEend))]

    LASCO_CME_time=[]
    for (x,y) in zip(year, LASCO_CME):
#        if y != b'' and y!=b'...':
        try:
            print("y: ", y)
            temp=str(x)+" "+y.decode('UTF-8')[0:10]
            LASCO_CME_time.append(datetime.strptime(temp, "%Y %m/%d %H%M"))

        except:
            LASCO_CME_time.append("")
 
    CRicmes['Disturbance']=Disturbance_time
    CRicmes['ICMEstart']=ICMEstart_time
    CRicmes['ICMEend']=ICMEend_time
    CRicmes['LASCO_CME']=LASCO_CME_time#, dtype=datetime64

     
#    print(CRicmes['LASCO_CME'])
    print(CRicmes)

#    print(CRicmes['year'])
    
    
    
    
    
    
main()