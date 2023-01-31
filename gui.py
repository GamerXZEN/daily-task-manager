from functions import read_tasks, write_tasks
import PySimpleGUI as sg

label = sg.Text("Type in a task to do today")
input_box = sg.InputText(tooltip="Enter task here")

add_button = sg.Button("Add Task")
edit_button = sg.Button("Edit Task")
complete_button = sg.Button("Complete Task")
exit_button = sg.Button("Exit Task")

desktop_window = sg.Window("Daily Task Manager", layout=[[label], [input_box, add_button]])

desktop_window.read()
desktop_window.close()
