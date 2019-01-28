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

