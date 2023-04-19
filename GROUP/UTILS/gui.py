import pandas as pd
import PySimpleGUI as sg

# Load the data
data = pd.read_csv('mydata_sorted.csv')

# Function to display the dataset


def show_dataset():
    header_list = list(data.columns)
    data_list = data.head(10).values.tolist()

    layout_table = [
        [sg.Table(values=data_list, headings=header_list, display_row_numbers=False, auto_size_columns=True,
                  num_rows=min(25, len(data_list)), alternating_row_color='lightblue', key='-TABLE-')]
    ]

    window_table = sg.Window("Dataset", layout_table)
    event, _ = window_table.read()
    window_table.close()


# Define the GUI layout
layout = [
    [sg.Text("Luxury Hotel Price Scraper for Geneva")],
    [sg.Button("Show Dataset", key="SHOW_DATASET")],
]

# Create the window
window = sg.Window("Luxury Hotel Price Scraper", layout)

# Event loop


def gui():
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "SHOW_DATASET":
            show_dataset()

# Close the window
    window.close()
