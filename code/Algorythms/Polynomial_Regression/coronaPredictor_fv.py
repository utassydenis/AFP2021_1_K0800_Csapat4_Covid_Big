import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
import csv


def Predictor(day: int, column: str, data: str):
    file = open(data + ".csv")
    reader = csv.reader(file)
    lines = int(len(list(reader))) - 1
    print('Number of rows: ', lines)

    data = pd.read_csv(data + '.csv', sep=';')
    data = data[['day', column]]
    print('-' * 30);
    print('HEAD');
    print('-' * 30)
    print(data.head())

    print('-' * 30);
    print('PREPARE DATA');
    print('-' * 30)
    x = np.array(data['day']).reshape(-1, 1)
    y = np.array(data[column]).reshape(-1, 1)
    plt.plot(y, '-m')

    polyFeat = PolynomialFeatures(degree=4)
    x = polyFeat.fit_transform(x)

    print('-' * 30);
    print('TRAINING DATA');
    print('-' * 30)
    model = linear_model.LinearRegression()
    model.fit(x, y)
    accuracy = model.score(x, y)
    print(f'Accuracy:{round(accuracy * 100, 3)} %')
    y0 = model.predict(x)

    days = day
    print('-' * 30);
    print('PREDICTION');
    print('-' * 30)
    print(f'Prediction - Cases after {days} days: ', end='')
    print(round(int(model.predict(polyFeat.fit_transform([[lines + days]])))), 'people')

    x1 = np.array(list(range(1, lines + days))).reshape(-1, 1)
    y1 = model.predict(polyFeat.fit_transform(x1))

    plt.title('Modell')
    plt.xlabel('Napok')
    plt.ylabel('Megbetegedések')
    plt.legend(['Eredeti'])
    plt.plot(y1, '--r')
    plt.plot(y0, '--b')
    plt.show()


Predictor(20, "cases", "covid_hungary")
