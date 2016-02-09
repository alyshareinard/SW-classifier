# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:31:29 2016

@author: alysha.reinard
"""

#import numpy as np
import csv
import pickle
#from sklearn.cross_validatation import train_test_split

with open("combined1hr.p", "rb") as f:
    combined1hr=pickle.load(f)
    # use combined1hr.dtype.names to see what's inside
    # use combined1hr['year'] to swee what's in the year column
data = combined1hr[['proton_temp', 'proton_speed', 'He4toprotons', \
    'proton_density', 'O7to6', 'avqFe', 'nHe2']]


    
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    

    
    