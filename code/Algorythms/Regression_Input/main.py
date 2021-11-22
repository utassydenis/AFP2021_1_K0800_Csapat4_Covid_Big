import pandas as pd
from matplotlib import pyplot as plt

raw_data = pd.read_excel('D:\CovidProj\hun.xlsx')

total_cases = raw_data['total_cases']
total_deaths = raw_data['total_deaths']
plt.scatter(total_cases,total_deaths,label='Raw Data')
plt.title('Cases vs Deaths')
plt.xlabel('Cases')
plt.ylabel('Deaths')
plt.show()

parameters = {'alpha' : 1000, 'beta' : 500}

def y_hat(cases,params):
    alpha = params['alpha']
    beta = params['beta']
    return alpha + beta * cases
y_hat(5,parameters)


def learn_parameters(data,params):
    x,y = data['total_cases'], data['total_deaths']
    x_bar, y_bar = x.mean(), y.mean()
    x,y = x.to_numpy(), y.to_numpy()
    beta = sum( ((x-x_bar) * (y-y_bar)) / sum((x-x_bar)**2))
    alpha = y_bar - beta * x_bar
    params['alpha'] = alpha
    params['beta'] = beta

new_parameter = {'alpha' : -2, 'beta' : 1000}
learn_parameters(raw_data,new_parameter)

spaced_cases = list(range(7000)) #NEM LEHET 19!
spaced_untrained_predictions = [y_hat(x,parameters) for x in spaced_cases]

cases = raw_data['total_cases']
deaths = raw_data['total_deaths']

spaced_trained_predictions = [y_hat(x,new_parameter) for x in spaced_cases]
plt.scatter(cases,deaths,label='Raw Data')
plt.title('Cases vs Deaths')
plt.xlabel('Cases')
plt.ylabel('Deaths')


new_cases = int(input('Enter cases to predict deaths: '))
print(y_hat(new_cases,new_parameter))



