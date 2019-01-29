#import library
#mathematic library
import numpy as np
#ploting library
import matplotlib.pyplot as plt
#managing data set
import pandas as pd


#importing data set     
dataset = pd.read_csv('Data.csv')
#selecting the first three columns
X = dataset.iloc[:, :-1].values

y = dataset.iloc[:, 3].values


#taking care of missed data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN' , strategy ='mean', axis =0)
### calculates the mean
imputer.fit(X[:, 1:3])
### put it in the matrics
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding categorical data

