def get_todos(filepath):
    with open(filepath) as file_local:
        todos_local = file_local.readlines()

        return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)