import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

blue_cli = "\033[34m"

# Load the data from the CSV file
data = pd.read_csv('mydata_sorted.csv')

# Remove leading/trailing spaces from column names
data.columns = data.columns.str.strip()

# Display the first few rows of the data
# print(data.head())

# Convert the timestamp to a numerical feature (time difference in hours)
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Timestamp'] = (data['Timestamp'] -
                     data['Timestamp'].min()) / np.timedelta64(1, 'h')

# Define a function to clean the prices by removing non-numeric characters and converting to float


def clean_price(price_str):
    return float(price_str.replace('\n', '').replace('€', '').replace(',', '').strip())


# def make_linear_regression(room_type_name):
#     # Clean the room_type_name column by applying the clean_price function
#     data[room_type_name] = data[room_type_name].apply(clean_price)

#     # Set the independent variable (X) to 'Timestamp' and the dependent variable (Y) to room_type_name
#     X = data[['Timestamp']].set_axis(['Timestamp'], axis=1)  # Set feature names
#     Y = data[room_type_name]

#     # Split the data into training (80%) and testing (20%) sets
#     X_train, X_test, Y_train, Y_test = train_test_split(
#         X, Y, test_size=0.2, random_state=0)

#     # Create a linear regression model
#     linear_regression = LinearRegression()

#     # Fit the model to the training data
#     linear_regression.fit(X_train, Y_train)

#     # # Make predictions on the test data
#     # Y_pred = linear_regression.predict(X_test)

#     # Predict the price for tomorrow
#     last_timestamp = data['Timestamp'].max()
#     next_timestamp = last_timestamp + 24  # Add 24 hours for the next day
#     tomorrow_price = linear_regression.predict([[next_timestamp]])

#     print(f"\n{blue_cli}The expected price for {room_type_name} tomorrow: €{tomorrow_price[0]:.2f}\n")

def make_linear_regression(room_type_name):
    # Clean the room_type_name column by applying the clean_price function
    data[room_type_name] = data[room_type_name].apply(clean_price)

    # Set the independent variable (X) to 'Timestamp' and the dependent variable (Y) to room_type_name
    X = data[['Timestamp']].to_numpy()  # Convert DataFrame to NumPy array
    Y = data[room_type_name]

    # Split the data into training (80%) and testing (20%) sets
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=0)

    # Create a linear regression model
    linear_regression = LinearRegression()

    # Fit the model to the training data
    linear_regression.fit(X_train, Y_train)

    # Make predictions on the test data
    Y_pred = linear_regression.predict(X_test)

    # Predict the price for tomorrow
    last_timestamp = data['Timestamp'].max()
    next_timestamp = last_timestamp + 24  # Add 24 hours for the next day
    tomorrow_price = linear_regression.predict(np.array([[next_timestamp]]))

    print(f"\nThe expected price for {room_type_name} tomorrow: €{tomorrow_price[0]:.2f}\n")
