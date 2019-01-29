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
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features =[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

#splitting for train and test sets
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.2, random_state=0)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
##there is no need to fit for the test?
X_test = sc_X.transform(X_test) 
