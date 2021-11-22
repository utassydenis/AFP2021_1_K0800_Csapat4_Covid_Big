import inline as inline
import matplotlib
import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


dataset = pd.read_excel('D:\CovidProj\hungary.xlsx')
cleaned_data = dataset[dataset['total_deaths'] > 300]

#cleaned_data.plot(x='total_cases',y='total_deaths',style='o')
#plt.title('Cases vs Deaths')
#plt.xlabel('Cases')
#plt.ylabel('Deaths')
#plt.show()

plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.displot(cleaned_data['total_cases'])

X = cleaned_data['total_cases'].values.reshape(-1,1)
y = cleaned_data['total_deaths'].values.reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

y_pred = regressor.predict(X_test)

df = pd.DataFrame({'Actual': y_test.flatten(),'Predicted':y_pred.flatten()})
print(df)


#df1 = df.head(25)
#df1.plot(kind='bar',figsize=(16,10))
#plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#plt.show()

plt.scatter(X_test, y_test,color='gray')
plt.plot(X_test,y_pred,color='red',linewidth=2)
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))