import PySimpleGUI as sg
from converter import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inch_label = sg.Text("Enter inches: ")
inch_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

desktop_window = sg.Window("Converter",
                           layout=[[feet_label, feet_input],
                                   [inch_label, inch_input],
                                   [button, output_label]])

while True:
    event, values = desktop_window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    desktop_window["output"].update(value=f"{result} m", text_color="white")

    match event:
        case sg.WIN_CLOSED:
            break

desktop_window.close()
