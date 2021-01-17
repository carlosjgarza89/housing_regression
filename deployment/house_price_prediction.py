# Import Neccesary Packages

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Import linear model and empty house DF

with open('regression_model.pickle', 'rb') as file:
	linreg = pickle.load(file)

with open('house_data.pickle', 'rb') as file:
	X = pickle.load(file)

# Gather data from user input

print('_____') # Spacer for terminal readability

bedrooms = float(input('bedroom quantity: '))
bathrooms = float(input('bathroom quantity: '))
waterfront = float(input('waterfront property (y=1, n=0): '))
renovated = float(input('renovated (y=1, n=0): '))
condition = int(input('condition (1-5): '))
grade = int(input('grade (3-13): '))
yr_built = float(input('year built: '))
sqft_living = float(input('sq.ft of living area: '))
zipcode = int(input('zipcode: '))
latitude = float(input('latitude: '))
longitude = float(input('longitude: '))

# Fill in X

X['log_bed'] = np.log(bedrooms)
X['bathrooms'] = bathrooms
X['waterfront'] = waterfront
X['renovated'] = renovated
X['log_yr_built'] = np.log(yr_built)
X['log_sqft_living'] = np.log(sqft_living)
X['log_lat'] = np.log(latitude)
X['log_long'] = np.log(np.abs(longitude))

if condition != 1:
	condition_column = f'condition_{condition}'
	X[condition_column] = 1

if grade != 3:
	grade_column = f'grade_{grade}'
	X[grade_column] = 1

if zipcode != 98001:
	zip_column = f'zipcode_{zipcode}'
	X[zip_column] = 1

# returning results

price = np.exp(linreg.predict(X)[0])

print('_____')
print('estimated cost of property: $', round(price, 2))
print('_____')