FILEPATH = 'tasks.txt'


def read_tasks(file_path=FILEPATH):
    """
    Reads the file whose name that is inputted as the argument,
    makes a list of those items, and returns that list. Has a
    default argument: tasks.txt for the file_path parameter.
    """
    with open(file_path, 'r') as file_original:
        tasks_original = file_original.readlines()
    return tasks_original


def write_tasks(tasks_original, file_path=FILEPATH):
    """
    Overwrites the contents of the file that is inputted
    as the argument with the list that is inputted as the
    other argument. Has a default argument: tasks.txt for
    the file_path parameter.
    """
    with open(file_path, 'w') as file_original:
        file_original.writelines(tasks_original)
