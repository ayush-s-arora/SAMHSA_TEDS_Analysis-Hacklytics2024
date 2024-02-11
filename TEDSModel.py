import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report


TEDSdf = pd.concat(map(pd.read_csv, ['tedsa_puf_1992_1994.csv', 'tedsa_puf_1995_1999.csv', 'tedsa_puf_2000_2004.csv', 'tedsa_puf_2005_2009.csv', 'tedsa_puf_2010.csv', 'tedsa_puf_2011.csv', 'tedsa_puf_2012.csv', 'tedsa_puf_2013.csv', 'tedsa_puf_2014.csv', 'tedsa_puf_2015.csv', 'tedsa_puf_2016.csv', 'tedsa_puf_2017.csv', 'tedsa_puf_2018.csv', 'tedsa_puf_2019.csv', 'tedsa_puf_2020.csv', 'tedsa_puf_2021.csv']), ignore_index=True)

TEDSdf = TEDSdf[['AGE', 'ARRESTS', 'SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'DAYWAIT', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB', 'NOPRIOR']]

TEDSdf = TEDSdf.drop(TEDSdf[TEDSdf.eq(-9).any(axis=1)].index)

TEDSdf = TEDSdf.dropna()

TEDSdf.to_csv('CleanedCombinedTEDS.csv', index=False)


X = TEDSdf[['AGE', 'ARRESTS', 'SUB1', 'MARSTAT', 'EDUC', 'PRIMINC', 'DAYWAIT', 'FREQ1', 'FREQ_ATND_SELF_HELP', 'HLTHINS', 'FRSTUSE1', 'RACE', 'SERVICES', 'PSYPROB']]
y = TEDSdf['NOPRIOR']

# Multiple Linear Regression - Really bad (R^2 = 0.1538913!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state=0)

regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)


y_predicted = regr.predict(X_test)

fig, ax = plt.subplots()
ax.scatter(y_predicted, y_test, edgecolors=(0, 0, 1))
ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=3)
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
plt.show()


mae = metrics.mean_absolute_error(y_test, y_predicted)
mse = metrics.mean_squared_error(y_test, y_predicted)
r2 = metrics.r2_score(y_test, y_predicted)

print("The model performance for testing set")
print("--------------------------------------")
print('MAE is {}'.format(mae))
print('MSE is {}'.format(mse))
print('R2 score is {}'.format(r2))