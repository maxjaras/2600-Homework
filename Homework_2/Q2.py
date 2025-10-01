from xml.parsers.expat import model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

Bikeshare_hours = pd.read_csv('Data/Bikeshare/hour.csv')
Bikeshare_days = pd.read_csv('Data/Bikeshare/day.csv')

x = Bikeshare_days['temp']
y = Bikeshare_days['cnt']
X = sm.add_constant(x)

## A residual plot for the daily data of biker count vs temperature ##

#model = sm.OLS(y, X).fit()
#fig, ax = plt.subplots()

#y_predicted = model.predict(X)
#residuals = y - y_predicted

#ax.scatter(y_predicted, residuals, alpha=0.3)
#ax.axhline(0, color='red', linestyle='--')
#ax.set_xlabel('Predicted Biker Count')
#ax.set_ylabel('Residuals')


## scatterplot with a regression line for the daily data of biker count vs temperature ##

#ax.scatter(Bikeshare_days['temp'], Bikeshare_days['cnt'], alpha=0.3)
#intercept = model.params['const']
#slope = model.params['temp']
#ax.axline((0,intercept), slope=slope, color='red')

#ax.set_xlabel('Temperature')
#ax.set_ylabel('Biker Count')

#print(model.summary())


## plot showing the temperature vs biker count ##

#plt.ylabel('Biker Count')
#plt.xlabel('Temperature')
#plt.scatter(Bikeshare_hours['temp'], Bikeshare_hours['cnt'], alpha=0.3)

plt.show()


## the predicted biker count on the day with the lowest average temp ##

#min_temp = Bikeshare_days['temp'].min()
#predicted_min = model.predict([1, min_temp])[0]
#print(predicted_min)