import PySimpleGUI as sg

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input()

inch_label = sg.Text("Enter inches: ")
inch_input = sg.Input()

desktop_window = sg.Window("Converter",
                           layout=[[feet_label, feet_input],
                                   [inch_label, inch_input]])

desktop_window.read()
desktop_window.close()