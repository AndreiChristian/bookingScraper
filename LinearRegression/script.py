import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def clean_price(price):
    return float(price.replace("€", "").replace(",", "").strip())


data = pd.read_csv("../GROUP/mydata_sorted.csv")
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Clean the price columns
for col in ['Standard', 'Superior', 'Junior Suite', 'Suite']:
    data[col] = data[col].apply(clean_price)

data['Hours'] = data['Timestamp'].dt.hour + data['Timestamp'].dt.minute / 60

room_types = ['Standard', 'Superior', 'Junior Suite', 'Suite']

for room_type in room_types:
    print(f"Performing linear regression for {room_type}:")

    X = data['Hours'].values.reshape(-1, 1)
    Y = data[room_type].values.reshape(-1, 1)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)

    print(f"Mean squared error: {mse:.2f}")
    print(f"R-squared score: {r2:.2f}")
    print(f"Intercept: {model.intercept_[0]:.2f}")
    print(f"Coefficient: {model.coef_[0][0]:.2f}")
    print("\n")
