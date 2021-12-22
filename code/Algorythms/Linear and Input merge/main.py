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

#### TRAINING DATA ####
print('-'*30);print('TRAINING DATA');print('-'*30)
model = linear_model.LinearRegression()
model.fit(x, y)
accuracy = model.score(x, y)
print(f'Accuracy:{round(accuracy*100,3)} %')
y0 = model.predict(x)
# plt.plot(y0, '--b')
# plt.show()

