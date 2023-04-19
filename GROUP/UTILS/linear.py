import pandas as pd
from sklearn.linear_model import LinearRegression

# Read the preprocessed CSV file using pandas
data = pd.read_csv('your_preprocessed_file_name.csv')

# Separate the independent variable(s) (X) and dependent variable (y)
X = data.iloc[:, 1:].values # Use all columns except the first (timestamp)
y = data.iloc[:, 1].values # Use the second column (Standard)

# Create a LinearRegression object and fit the data
regressor = LinearRegression()
regressor.fit(X, y)

# Print the coefficients of the linear regression model
print(regressor.coef_)
