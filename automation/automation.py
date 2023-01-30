with open('files.txt', 'r') as file:
    filenames = file.readlines()

for filename in filenames:
    filename = filename.strip('\n')
    with open(filename, 'w') as file:
        file.write('Hello')