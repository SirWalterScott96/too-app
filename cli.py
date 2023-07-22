from function import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')
print(now)

while True:
    user_action = input('Enter add, show, edit or stop: ')
    user_action = user_action.strip()

    if user_action.startswith('add') or 'new' in user_action:
        todo = user_action[4:]

        todos = get_todos('files/todos.txt')

        todos.append(todo + '\n')

        write_todos('files/todos.txt', todos)


    elif user_action.startswith('show'):

        todos = get_todos('files/todos.txt')

        for index, item in enumerate(todos, 1):
            item = item.strip('\n')
            print(index, '-', item, sep='')

    elif user_action.startswith('stop'):
        break
    elif 'edit' in user_action:
        try:
            number = int(input('Number of the todo to edit: '))
            number = number - 1

            todos = get_todos('files/todos.txt')

            todos.append(todo + '\n')

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)

        except ValueError:
            print('Your command is not valid')
            continue

print('Bye!')


