import os
import csv
import numpy as np
import random
import pandas as pd
import time
import matplotlib.pyplot as plt

csv_lines = [] #preallocate list for extracted csv lines

path_to_csv = "data/dataset.csv"

raw_data = pd.read_csv(path_to_csv, sep=';')

# encode as nominal
#raw_data.user.unique(); raw_data.user = raw_data.user.map({'debora':0, 'katia':1, 'wallace':2, 'jose_carlos':3}); raw_data.user.unique()
raw_data.gender.unique(); raw_data.gender = raw_data.gender.map({'Woman':1, 'Man':0}); raw_data.gender.unique()

raw_data['how_tall_in_meters'] = raw_data['how_tall_in_meters'].str.replace(',', '.')
raw_data['body_mass_index'] = raw_data['body_mass_index'].str.replace(',', '.')

raw_data[pd.isnull(raw_data).any(axis=1)]

raw_data.isnull().values.any(); raw_data.isnull().sum().sum()

raw_data.drop(raw_data[raw_data.z4 == "-14420-11-2011 04:50:23,713"].index.values, inplace=True) # row 122076 -> (165633, 19)
raw_data.z4 = pd.to_numeric(raw_data.z4, errors='raise'); raw_data.dtypes # z4 object -> int64
raw_data.columns

raw_data[pd.isnull(raw_data).any(axis=1)]

raw_data = raw_data[raw_data['body_mass_index'].notnull()]

raw_data[pd.isnull(raw_data).any(axis=1)]

raw_data.isnull().values.any(); raw_data.isnull().sum().sum()

# y - label 

y = raw_data['class'].copy()
type(y); y.describe(); y.head(3); y.shape; y.unique() # (165632, )

y = y.map({'sitting':0, 'sittingdown':1, 'standing':2, 'standingup':3, 'walking':4})

raw_data.drop(labels=['user', 'gender', 'age', 'how_tall_in_meters', 'weight', 'body_mass_index', 'class'], axis=1, inplace=True); raw_data.shape 

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import  recall_score, precision_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# thang đo MSE, F-measure, precision, recall, accuracy

X_train, X_test, y_train, y_test = train_test_split(raw_data.sample(n = 10000, random_state=1), y.sample(n = 10000, random_state=1), test_size=0.30, random_state=7)
X_train.shape, X_test.shape, y_train.shape, y_test.shape 

best_accu = 0
best_neighbor = 0
best_precision = 0
best_recall = 0
best_mse = 0
best_time = 0
print("Finding best \"neighbor\" hyperparam..")
for neighbor in range(1,30):
    model = KNeighborsClassifier(n_neighbors=neighbor)
    s= time.time()
    model.fit(X_train, y_train)
    done = time.time() - s
    y_pred = model.predict(X_test)
    accu = accuracy_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='macro')
    precision = precision_score(y_test, y_pred, average='macro')
    if best_accu < accu:
        best_neighbor = neighbor
        best_accu = accu
        best_mse = mse
        best_precision = precision
        best_recall = recall
        best_time = done







#print("Fitting completed in: ", done)
#print('MSE = ', mse)
#print(classification_report(y_test, y_pred))

import pickle

# save the model to disk

filename = 'model/KNN.sav'
pickle.dump(model, open(filename, 'wb'))
 
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

def predict_for_instance(x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4):
    instance = np.array([x1,y1,z1,x2,y2,z2,x3,y3,z3,x4,y4,z4]).reshape(1,-1)
    predicted_value = loaded_model.predict(instance)
    
    return (predicted_value)

def solve(choosen):
    raw_data = pd.read_csv('data/dataset.csv', sep=';')
    raw_data.gender.unique(); raw_data.gender = raw_data.gender.map({'Woman':1, 'Man':0}); raw_data.gender.unique()
    raw_data['how_tall_in_meters'] = raw_data['how_tall_in_meters'].str.replace(',', '.')
    raw_data['body_mass_index'] = raw_data['body_mass_index'].str.replace(',', '.')
    raw_data['z4'] = pd.to_numeric(raw_data['z4'], errors='coerce')
    raw_data = raw_data.dropna(how='any')
    data = raw_data.sample(choosen)
    y = data['class'].copy()
    type(y); y.describe(); y.head(3); y.shape; y.unique() # (165632, )
    y = y.map({'sitting':0, 'sittingdown':1, 'standing':2, 'standingup':3, 'walking':4})
    data.drop(labels=['user', 'gender', 'age', 'how_tall_in_meters', 'weight', 'body_mass_index', 'class'], axis=1, inplace=True)
    y_pred = loaded_model.predict(data)
    acc = accuracy_score(y, y_pred)

    return acc