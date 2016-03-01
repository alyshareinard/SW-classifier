"""
Created on Wed Feb  3 14:31:29 2016
@author: alysha.reinard
"""

import numpy as np
#import csv
import pickle
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt

f=open('combined1hr_wdate.p', 'rb')
combined_data=pickle.load(f)
f.close()
f=open('CR_icmes.p', 'rb')
CR_icmes=pickle.load(f)
f.close()

#determine which time periods in combined_data are also in CR_icmes

try:
    f=open('is_cme.p', 'rb')
    is_cme=pickle.load(f)
    f.close()
except:
    is_cme=[]
    for date in combined_data["datetime"]:
        print(date)
        cme_val=0
        for i in range(len(CR_icmes)):
            if date > CR_icmes["ICMEstart_datetime"][i] and date < CR_icmes["ICMEend_datetime"][i]:
                cme_val=1
        
        is_cme.append(cme_val)
        filehandler=open('is_cme.p', 'wb')
        pickle.dump(is_cme, filehandler)   
        
#is_CME 0 = slow, 1 = ICME

print(len(is_cme))
print(len(combined_data))

proton_speed=[i for i in combined_data["proton_speed"]]
proton_temp=[i for i in combined_data["proton_temp"]]

X=np.asarray([proton_speed,proton_temp]).T

#from learning scikitlearn book
X_train, X_test, y_train, y_test = train_test_split(X, is_cme, test_size=0.25, random_state=33)
#standardize the features -- subtract mean, divide by std
scaler=preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test=scaler.transform(X_test)

xs_cme=[]
ys_cme=[]
xs_slow=[]
ys_slow=[]
for index, item in enumerate(y_train):
    if item==1:
        xs_cme.append(X_train[index,0])
        ys_cme.append(X_train[index,1])
    elif item==0:
        xs_slow.append(X_train[index,0])
        ys_slow.append(X_train[index,1])
    
#xs_cme=X_train[:,0][y_train==1]
#ys_cme=X_train[:,1][y_train==1]

#xs_slow=X_train[:,0][y_train==0]
#ys_slow=X_train[:,1][y_train==0]

plt.scatter(xs_slow, ys_slow, c="blue")
plt.scatter(xs_cme, ys_cme, c="red")

plt.xlim((0, 0.6))
plt.xlabel('speed')
plt.ylabel('temp') 

#linear classifier
from sklearn.linear_model import SGDClassifier
clf=SGDClassifier()
clf.fit(X_train, y_train)
print(clf.coef_)
print(clf.intercept_)
x_min, x_max = X_train[:,0].min() - .5, X_train[:,0].max() + 0.5
xs=np.arange(x_min, x_max, 0.5)
ys=clf.intercept_ + xs*clf.coef_[0][0]
plt.plot(xs, ys, hold=True)

#evaluating results
from sklearn import metrics
y_train_pred = clf.predict(X_train)
print("accuracy score - training data: ", metrics.accuracy_score(y_train, y_train_pred))

y_test_pred = clf.predict(X_test)
print("accuracy score - test data: ", metrics.accuracy_score(y_test, y_test_pred))

print("classification report", metrics.classification_report(y_test, y_test_pred))

print("confusion matrix", metrics.confusion_matrix(y_test, y_test_pred))