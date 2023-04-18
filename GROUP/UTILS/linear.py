import pandas as pd
from sklearn.linear_model import LinearRegression

# Define the data as a pandas DataFrame
data = pd.DataFrame([
    ["Mandarin Oriental", 803, 874, 1078, 1282],
    ["Four Seasons Geneva", 1155, 1369, 1751, 3861],
    ["Hotel d'Angleterre", 721, 1078, 2251, 4799],
    ["Intercontinental Geneve", 624, 747, 1236, 7251],
    ["Ritz Carlton Hotel de la Paix", 925, 1078, 1537, 2149],
    ["Beau Rivage Geneva", 747, 808, 1409, 2327],
    ["Fairmont Hotel", 833, 1267, 1267, 5105]
], columns=["Hotel", "Standard", "Superior", "Junior Suite", "Suite"])

# Separate the input and output variables
X = data.drop("Hotel", axis=1)
y = data["Suite"] # Change this to the category you want to predict for

# Create the model
model = LinearRegression()
model.fit(X, y)

# Predict the prices for tomorrow
predicted_prices = model.predict(X)

# Print the predicted prices
print(predicted_prices)
