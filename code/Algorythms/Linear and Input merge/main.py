import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

#### LOAD DATA ####
data = pd.read_csv('covid_hungary.csv', sep=';')
data = data[['day', 'cases']]
print('-'*30);print('HEAD');print('-'*30)
print(data.head())

