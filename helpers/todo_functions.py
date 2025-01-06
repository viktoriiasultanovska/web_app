import helpers.file as file_helper


def add_todo(new_todo):
    todos = file_helper.read_file()
    todos.append(new_todo)
    file_helper.write_file(todos)


def get_todos():
    return file_helper.read_file()


def write_todos(todos):
    file_helper.write_file(todos)
