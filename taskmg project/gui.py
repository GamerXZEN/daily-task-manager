from functions import read_tasks, write_tasks
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

time_label = sg.Text("", key="clock")
label = sg.Text("Type in a task to do today")
input_box = sg.InputText(tooltip="Enter task here", key="task")

add_button = sg.Button("Add Task", size=10)
edit_button = sg.Button("Edit Task")
complete_button = sg.Button("Complete Task")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=read_tasks(), key="tasks",
                      enable_events=True, size=(45, 10))

desktop_window = sg.Window("Daily Task Manager",
                           layout=[[time_label],
                                   [label], [input_box, add_button],
                                   [list_box, edit_button, complete_button],
                                   [exit_button]],
                           font=("Helvetica", 12))

while True:
	event, values = desktop_window.read(timeout=10)
	desktop_window["clock"].update(value=time.strftime("%B %d, %Y %H:%M:%S"))

	match event:
		case "Add Task":
			tasks = read_tasks()
			new_task = values["task"] + "\n"

			tasks.append(new_task)
			write_tasks(tasks)

			desktop_window["tasks"].update(values=tasks)

		case "Edit Task":
			try:
				task_to_edit = values["tasks"][0]
				new_task = values["task"]

				tasks = read_tasks()
				task_index = tasks.index(task_to_edit)
				tasks[task_index] = new_task + "\n"
				write_tasks(tasks)

				desktop_window["tasks"].update(values=tasks)

			except IndexError:
				sg.Popup("Please select an item first.", font=("Helvetica", 12))
				continue

		case "Complete Tasks":
			try:
				complete_task = values["tasks"][0]
				tasks = read_tasks()

				tasks.remove(complete_task)
				write_tasks(tasks)
				desktop_window["tasks"].update(values=tasks)
				desktop_window["task"].update(value="")
			except IndexError:
				sg.Popup("Please select an item first.", font=("Helvetica", 12))
				continue

		case "tasks":
			desktop_window["task"].update(value=values["tasks"][0])

		case "Exit":
			break

		case sg.WIN_CLOSED:
			break

desktop_window.close()
