# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 16:01:46 2016

@author: alysha.reinard
"""

from pylab import *

from sklearn.datasets import fetch_20newsgroups
news=fetch_20_newsgroups(subset='all')

SPLIT_PERC=0.75
split_size=int(len(news.data)*SPLIT_PERC)
X_train=news.data[:split_size]
X_test=news.data[split_size:]
y_train=news.data[:split_size]
y_test=news.data[split_size:]

