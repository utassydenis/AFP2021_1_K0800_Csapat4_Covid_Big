import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
%matplotlib inline
import statsmodels.api as sm
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
cf.go_offline()

import requests
from bs4 import BeautifulSoup
import json
from pandas import DataFrame as df

#############
owid_df = pd.read_csv('./owid-covid-data.csv')

owid_df.columns # Összes oszlop megjelenítése

# Tömb létrehozása az országoknak
covid_df = owid_df.location.unique()
# Indexelés az USA-nak
indexer = owid_df[owid_df['location']=='United States'].index
# Adatgyüjtés az ország számára
covid_df = owid_df.loc[indexer, 'date':'new_deaths_per_million']
# Törlni a NaN értékeket
covid_df = covid_df.dropna()
# Dátum beállítása indexeléshez
covid_df.set_index('date', inplace=True)
# Összes oszlop törlése kivéve amelyiket én akarom
covid_df.drop(covid_df.columns.difference(['new_deaths_per_million']), 1, inplace=True)
covid_df.plot(figsize=(12,6))
# 30napos mozgási tartomány beállítása
covid_df.rolling(window=30).mean()['new_deaths_per_million'].plot()

covid_df = covid_df.asfreq('d') # Gyakoriság beállítása napira
# covid_df = covid_df.set_index('date').asfreq('d')
# Annak az adatoknak a száma amivel rendelkezünk
covid_df.info() # 241 : 192 Training : 49 Test
# 2 részre való különítés
train_df = covid_df.iloc[:192]
test_df = covid_df.iloc[191:]

covid_df.index
##############
# The Holt - Winters Method 3 nézőpontra bontja a
# idősorokat átlag, iránya és szezonalitás.
# Összeségében próbálja megjóslni a jövőbeliségét,
# időszakossága és ismétlőségével a sorozatnak.

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Nincs exponenciális növekedés ezért én adom meg
# 14-et választottam a legjobb erdemény érdekében
fit_model = ExponentialSmoothing(train_df['new_deaths_per_million'],
                                  trend='add',
                                  seasonal='add',
                                  seasonal_periods=14).fit()
# 50 napos előrejelzést tudunk csinálni
prediction = fit_model.forecast(50)
prediction

# Képzési, tesztelési és és vetítési adatok ábrázolása
train_df['new_deaths_per_million'].plot(figsize=(12,6))
test_df['new_deaths_per_million'].plot()
prediction.plot(xlim=['2020-09-09','2020-10-28'])

##############################

def mae(y1, y2, axis=0):
    y1_np = y1.to_numpy()
    y2_np = y2.to_numpy()
    return np.mean(np.abs(y1_np - y2_np), axis=axis)

mae(test_df, prediction, None)

from sklearn.metrics import mean_absolute_error, mean_squared_error

mean_absolute_error(test_df, prediction)
# test_df.mean() # az adatunk jó-e

################################

def mse(y1, y2, axis=0):
    y1_np = y1.to_numpy()
    y2_np = y2.to_numpy()
    return ((y1_np - y2_np) ** 2).mean(axis=axis)


mse(test_df, prediction, None)

mean_squared_error(test_df, prediction)

################################

np.sqrt(mean_squared_error(test_df, prediction))

################################

covid_model = ExponentialSmoothing(covid_df['new_deaths_per_million'],
                                  trend='add',
                                  seasonal='add',
                                  seasonal_periods=14).fit()
# 100 napos előrejelzés
covid_forecast = covid_model.forecast(100)
# Kiiratjuk az eredetit, aztán a mi jóslatunkat is
covid_df.plot(figsize=(12,6))
covid_forecast.plot()

####################################