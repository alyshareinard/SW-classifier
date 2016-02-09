# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:23:13 2016

@author: alysha.reinard
"""
import csv
import numpy as np

def main():
    names=['year', 'Disturbance', 'ICME', 'Composition', 'MCstartend', 'BDE', 'BIF', \
    'Qual.', 'dV', 'V_ICME',	'V_max', 'Bfield', 'MC', 'Dst', 'V_transit', \
    'LASCO_CME']

    with open("icmetable2.csv", "rt") as f:    
        reader=csv.reader(f, delimiter=',')
        names=reader.__next__()
    print(names)
    CRicmes=np.genfromtxt("icmetable2.csv", delimiter=',', names=names, \
    dtype=(int, 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', 'S10', \
    'S10', int, int, int, 'S10', int, int, 'S10', 'S10'), missing_values=None)
    print(CRicmes['year'])
    
    
    
    
    
    
main()