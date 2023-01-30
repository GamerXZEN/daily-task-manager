from functions import read_tasks, write_tasks

while True:
    user_input = input('Do you want to add, show, edit, complete, or exit: ').lower().strip()

    if 'add' in user_input[:4]:
        if user_input.lower() == 'add':
            task = input('Enter your task: ') + '\n'
            tasks = read_tasks()
            tasks.append(task.title())

        else:
            task = user_input[4:].strip('\n')
            tasks = read_tasks()
            tasks.append(task.title() + '\n')
            write_tasks(tasks)

    elif 'show' in user_input[:5]:
        tasks = read_tasks()
        for index, item in enumerate(tasks):
            item = item.strip('\n')
            print(f"{index + 1}. {item}")

    elif 'edit' in user_input[:5]:
        if user_input.lower() == 'edit':
            number = int(input('Number of the task to edit: ')) - 1

            new_task = input('Enter your new task: ') + '\n'
            tasks = read_tasks()
            tasks[number] = new_task
            write_tasks(tasks)

        else:
            try:
                number = int(user_input[5:])

                new_task = input('Enter your new task: ') + '\n'
                tasks = read_tasks()
                tasks[number] = new_task
                write_tasks(tasks)

            except ValueError:
                print('Your input is invalid')
                continue

    elif 'complete' in user_input[:9]:
        if user_input.lower() == 'complete':
            tasks = read_tasks()

            task_input = int(user_input[9:])
            print("Removed", tasks[task_input].strip('\n'))
            tasks.pop(task_input)
            write_tasks(tasks)

        else:
            try:
                tasks = read_tasks()

                task_input = int(input('What is the number of task you completed: ')) - 1
                print("Removed", tasks[task_input].strip('\n'))
                tasks.pop(task_input)
                write_tasks(tasks)

            except IndexError:
                print('There ix no task that is located at that index.')
                continue

    elif 'exit' in user_input[: 5]:
        exit('Program terminated. KeyboardInterrupt or UserExitException')

    else:
        print('Invalid input')
