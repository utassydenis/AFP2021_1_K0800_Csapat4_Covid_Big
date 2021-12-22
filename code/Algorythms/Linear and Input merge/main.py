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

#### PREDICTION ####
days = 14
print('-'*30);print('PREDICTION');print('-'*30)
print(f'Prediction - Cases after {days} days: ', end='')
print(round(int(model.predict(polyFeat.fit_transform([[284 + days]])))), 'people')

x1 = np.array(list(range(1, 284+days))).reshape(-1, 1)
y1 = model.predict(polyFeat.fit_transform(x1))

plt.title('Modell')
plt.xlabel('Napok')
plt.ylabel('Megbetegedések')
plt.legend(['Eredeti'])
plt.plot(y1, '--r')
plt.plot(y0, '--b')
plt.show()


## Input Regression

cases = data['cases']
day = data['day']
plt.scatter(cases,day,label='Data')
plt.title('Cases vs Days')
plt.xlabel('Cases')
plt.ylabel('Days')
plt.show()

parameters = {'alpha' : 1000, 'beta':500}

def y_hat(cases,params):
    alpha = params['alpha']
    beta = params['beta']
    return alpha + beta * cases
y_hat(5,parameters)

def learn_parameters(data,params):
    x,y = data['cases'],data['day']
    x_bar,y_bar = x.mean(), y.mean()
    x,y = x.to_numpy(), y.to_numpy()
    beta = sum(((x-x_bar) * (y-y_bar)) / sum((x-x_bar)**2))
    alpha = y_bar - beta * x_bar
    params['alpha'] = alpha
    params['beta'] = beta

