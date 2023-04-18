import tkinter as tk
from tkinter import ttk

# Define the data as a list of tuples
data = [
    ("2023-04-18 16:21:00", "Mandarin Oriental", "€ 803", "€ 874", "€ 1,078", "€ 1,282"),
    ("2023-04-18 16:21:00", "Four Seasons Geneva", "€ 1,155", "€ 1,369", "€ 1,751", "€ 3,861"),
    ("2023-04-18 16:21:00", "Hotel d'Angleterre", "€ 721", "€ 1,078", "€ 2,251", "€ 4,799"),
    ("2023-04-18 16:21:00", "Intercontinental Geneve", "€ 624", "€ 747", "€ 1,236", "€ 7,251"),
    ("2023-04-18 16:21:00", "Ritz Carlton Hotel de la Paix", "€ 925", "€ 1,078", "€ 1,537", "€ 2,149"),
    ("2023-04-18 16:21:00", "Beau Rivage Geneva", "€ 747", "€ 808", "€ 1,409", "€ 2,327"),
    ("2023-04-18 16:21:00", "Fairmont Hotel", "€ 833", "€ 1,267", "€ 1,267", "€ 5,105")
]

# Define a function to create the GUI
def create_gui():
    # Create the root window
    root = tk.Tk()
    root.title("Hotel Room Rates")
    
    # Create the table
    table = ttk.Treeview(root)
    table["columns"] = ("standard", "superior", "junior_suite", "suite")
    table.heading("#0", text="Timestamp")
    table.heading("standard", text="Standard")
    table.heading("superior", text="Superior")
    table.heading("junior_suite", text="Junior Suite")
    table.heading("suite", text="Suite")
    
    # Add the data to the table
    for row in data:
        table.insert("", tk.END, text=row[0], values=row[1:])
    
    # Pack the table
    table.pack(expand=True, fill=tk.BOTH)
    
    # Start the main loop
    root.mainloop()

# Call the create_gui function to display the GUI
create_gui()
