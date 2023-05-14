# -*- coding: utf-8 -*-
"""1910040_Tasnia_CSE425_final_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SWdTB862-2fbqvpReEUyoABa0krGgONi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")
X = data[['Volume', 'Weight']]
y = data['CO2']

print(X)

volume = data['Volume']
weight = data['Weight']
print(weight)
print(volume)

#2a...normalizing weight
min_weight= weight.min()
#print(min_weight)
max_weight= weight.max()
#print(max_weight)
for i in range(0,36):
  weight[i]= (weight[i]-min_weight)/(max_weight-min_weight) 
print(weight)

#2a...normalizing volume
min_vol= volume.min()
print(min_vol)
max_vol= volume.max()
print(max_vol)
for i in range(0,36):
  volume[i]= (volume[i]-min_vol)/(max_vol-min_vol) 
print(volume)

X = pd.merge(volume,weight, suffixes=['Volume','Weight'],left_index= True, right_index=True)
# print(X)
X = X.to_numpy()
# print(X)

# slicing the data into train and test sets
X_train = X[:30]
#print('xtrain',X_train)

y_train = y[:30]
#print('ytrain', y_train)

X_test = X[30:]
#print('Xtest', X_test)

y_test = y[30:]

#print(y_test)
