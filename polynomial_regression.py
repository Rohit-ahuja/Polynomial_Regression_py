# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 22:10:23 2018

@author: OM SAI RAM
"""

#IMPORTING LIBRARIES
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORTING DATASET

dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split

#X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 0)

#Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_Y = StandardScaler()
Y_train = sc_Y.fit_transform(Y_train)"""