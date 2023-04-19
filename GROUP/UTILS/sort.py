import pandas as pd


def sortData():
    # Load the CSV file into a pandas DataFrame
    data = pd.read_csv("../example.csv")

# Sort the DataFrame by the name column in ascending order
    data_sorted = data.sort_values(by="name", ascending=True)

# Save the sorted data to a new CSV file
    data_sorted.to_csv("mydata_sorted.csv", index=False)
