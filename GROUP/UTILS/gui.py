import PySimpleGUI as sg

sg.theme('DarkTeal9')  # Set the theme

# Define the layout
layout = [[sg.Text('Enter your name:'), sg.Input(key='-NAME-')],
          [sg.Text('Select your favorite color:'),
           sg.Combo(['Red', 'Blue', 'Green'], key='-COLOR-')],
          [sg.Button('Submit'), sg.Button('Cancel')]]

# Create the window
window = sg.Window('My Simple GUI', layout)

# Event loop
while True:
    event, values = window.read()

    # If the user closes the window or clicks the Cancel button
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    # If the user clicks the Submit button
    if event == 'Submit':
        name = values['-NAME-']
        color = values['-COLOR-']
        sg.popup(f'Hello, {name}! Your favorite color is {color}.')

# Close the window
window.close()
