import PySimpleGUI as sg

# All the stuff inside your window. This is the PSG magic code compactor...
layout = [[sg.Text('pyStay. Find out today the prices of tommorow using our machine learning models')],
          [sg.Text('Enter something on Row 2'), sg.InputText()],
          [sg.OK(), sg.Exit()]]

# Create the Window
window = sg.Window('pyStay', layout)
# Event Loop to process "events"
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
