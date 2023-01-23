class Directory:
    name = ""
    files = list()
    directories = dict()

    def __init__(self, name):
        self.name = name


def change_directory(current_dir, directory_name):
    if directory_name == '..':
        print('Returning parent directory from current directory')
        # return parent directory

    current_dir = current_dir.directories[directory_name]

    return current_dir


print('\nOutput for challenge day 7\n')

current_dir = Directory('/')

with open('days/7/input_simple.txt') as file:
    lines = file.readlines()

for line in lines[1:]:
    if line.startswith("$ cd"):
        line_parts = line.split(' ')
        directory_name = line_parts[2]
        current_dir = change_directory(current_dir, directory_name)
    else:
        # is "ls" command or a line that follows it
        if line.startswith("dir"):
            line_parts = line.split(' ')
            dir_name = line_parts[1]
            new_directory = Directory(dir_name)
            current_dir.directories[dir_name] = new_directory
        else:
            print("is a file")
