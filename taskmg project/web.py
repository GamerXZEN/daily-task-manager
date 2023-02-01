import streamlit

from functions import read_tasks as rt, write_tasks as wt
import streamlit as sl

tasks = rt()


def add_task():
	loc_task = sl.session_state["new task"]
	tasks.append(loc_task + "\n")
	wt(tasks)


sl.title("Daily Task Manager")
sl.subheader("This is a web version of the Daily Task Manager©")
sl.write("This app is used to manage your daily tasks and to-do's")

for index, task in enumerate(tasks):
	checkbox = sl.checkbox(task, key=task)
	if checkbox:
		tasks.pop(index)
		wt(tasks)
		del sl.session_state[task]
		sl.experimental_rerun()
		

sl.text_input(label="", placeholder="Enter a task",
              on_change=add_task, key="new task")
