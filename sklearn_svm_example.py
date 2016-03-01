# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 14:56:49 2016

@author: alysha.reinard
"""

import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

from sklearn.datasets import fetch_olivetti_faces
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score, KFold
from sklearn import metrics

from scipy.stats import sem

faces=fetch_olivetti_faces()

print(faces.DESCR)

print(faces.keys())

print(faces.images.shape)
print(faces.data.shape)
print(faces.target.shape)

print(np.max(faces.data))
print(np.min(faces.data))

print(np.mean(faces.data))

def print_faces(images, target, top_n):
    #set up the figure size in inches
    fig=plt.figure(figsize=(12, 12))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)
    for i in range(top_n):
        #plot the images in a matrix of 20x20
        p=fig.add_subplot(20,20,i+1,xticks=[], yticks=[])
        p.imshow(images[i], cmap=plt.cm.bone)
        
        #label the image iwth the targer value
        p.text(0,14,str(target[i]))
        p.text(0,60,str(i))

print_faces(faces.images, faces.target, 20)

svc_1=SVC(kernel='linear')

X_train, X_test, y_train, y_test = train_test_split(faces.data, faces.target, 
            test_size=0.25, random_state=0)

def evaluate_cross_validation(clf, X, y, K):
    #create a k-flod cross validation interator
    cv=KFold(len(y), K, shuffle=True, random_state=0)
    #by default the score used is the one returned by score method of the estimator (accuracy)
    scores=cross_val_score(clf, X, y, cv=cv)
    print(scores)
    print("Mean score: {0:.3f} (+/-{1:.3f})".format(np.mean(scores), sem(scores)))

evaluate_cross_validation(svc_1, X_train, y_train, 5)

def train_and_evaluate(clf, X_train, X_test, y_train, y_test):
    clf.fit(X_train, y_train)
    print("Accuracy on training set", clf.score(X_train, y_train))
    print("Accuracy on testing set", clf.score(X_test, y_test))
    
    y_pred=clf.predict(X_test)
    
    print("Classification Report: ", metrics.classification_report(y_test, y_pred))
    print("Confusion Matrix: ", metrics.confusion_matrix(y_test, y_pred))
    
train_and_evaluate(svc_1, X_train, X_test, y_train, y_test)

#the index ranges of images with people with glasses

glasses=[(10,19), (30,32), (37,38), (50,59), (63,64), (69,69), (120,121), 
         (124,129), (130,139), (160,161), (164,169), (180, 182), (185, 185), 
         (189,189), (190,192), (194,194), (196,199), (260,269), (270,279),
         (300,309), (330,339), (358,359), (360,369)]
         
def create_target(segments):
    # create a new y array of target size initialized with zeros
    y=np.zeros(faces.target.shape[0])
    #put 1 in the specified segments
    for (start,end) in segments:
        y[start:end+1]=1
    return y
target_glasses = create_target(glasses)

#have to train/test again
X_train, X_test, y_train, y_test = train_test_split(faces.data, target_glasses, 
                test_size=0.25, random_state=0)
                
#now we create a new SVC classifier and train it with the new target vector 
#to tell the difference between people with and without glasses
svc_2=SVC(kernel='linear')

evaluate_cross_validation(svc_2, X_train, y_train, 5)
train_and_evaluate(svc_2, X_train, X_test, y_train, y_test)

#lets see if the classifier is good at telling faces with glasses from faces 
#without
#the person in 30-39 is sometimes with and sometimes without glasses
X_test=faces.data[30:40]
y_test=target_glasses[30:40]
select=np.ones(target_glasses.shape[0])
select[30:40]=0
X_train=faces.data[select==1]
y_train=target_glasses[select==1]
svc_3 = SVC(kernel = 'linear')
train_and_evaluate(svc_3, X_train, X_test, y_train, y_test)

