from pathlib import Path

FILES_DIR: str = 'files'


def get_project_dir():
    return Path(__file__).parent.parent


def get_file_path(filename):
    return f'{get_project_dir()}/{FILES_DIR}/{filename}'


def read_file(filename='todos.txt'):
    with open(get_file_path(filename), 'r') as file:
        todos = file.readlines()
    return todos


def write_file(todos, filename='todos.txt'):
    with open(get_file_path(filename), 'w') as file:
        file.writelines(todos)
