def read_tasks(file_path='tasks.txt'):
    """
    Reads the file whose name that is inputted as the argument,
    makes a list of those items, and returns that list. Has a
    default argument: tasks.txt for the file_path parameter.
    """
    with open(file_path, 'r') as file_original:
        tasks_original = file_original.readlines()
    return tasks_original


def write_tasks(tasks_original, file_path='tasks.txt'):
    """
    Overwrites the contents of the file that is inputted
    as the argument with the list that is inputted as the
    other argument. Has a default argument: tasks.txt for
    the file_path parameter.
    """
    with open(file_path, 'w') as file_original:
        file_original.writelines(tasks_original)
