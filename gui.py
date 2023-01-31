from functions import read_tasks, write_tasks
import PySimpleGUI as sg

label = sg.Text("Type in a task to do today")
input_box = sg.InputText(tooltip="Enter task here", key="task")

add_button = sg.Button("Add Task")
edit_button = sg.Button("Edit Task")
complete_button = sg.Button("Complete Task")
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=read_tasks(), key="tasks",
                      enable_events=True, size=(45, 10))

desktop_window = sg.Window("Daily Task Manager",
                           layout=[[label], [input_box, add_button],
                                   [list_box, edit_button]],
                           font=("Helvetica", 12))

while True:
	event, values = desktop_window.read()

	match event:
		case "Add Task":
			tasks = read_tasks()
			new_task = values["task"] + "\n"

			tasks.append(new_task)
			write_tasks(tasks)

			desktop_window["tasks"].update(values=tasks)
		case "Edit Task":
			task = values["tasks"]
			new_task = values["task"] + "\n"

			tasks = read_tasks()
			index = tasks.index(task)
			tasks[index] = new_task
			write_tasks(tasks)

			desktop_window["tasks"].update(values=tasks)

		case "tasks":
			desktop_window["todo"].update(value=values["tasks"][0])

		case "Exit":
			break

		case sg.WIN_CLOSED:
			break

desktop_window.close()
