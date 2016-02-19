# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:31:29 2016

@author: alysha.reinard
"""

#import numpy as np
#import csv
import pickle
#from sklearn.cross_validation import train_test_split
#from sklearn import preprocessing

f=open('combined1hr_wdate.p', 'rb')
combined_data=pickle.load(f)
f.close()
f=open('CR_icmes.p', 'rb')
CR_icmes=pickle.load(f)
f.close()

#determine which time periods in combined_data are also in CR_icmes

is_cme=[]
for date in combined_data["datetime"]:
    for i in range(len(CR_icmes)):
        if date > CR_icmes["ICMEstart"][i] and date < CR_icmes["ICMEend"][i]:
            is_cme.append("ICME")
        else:
            is_cme.append("slow")
    

print(len(is_cme))
print(len(combined_data))
#    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    

    
    