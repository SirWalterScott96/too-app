import function
import PySimpleGUI as sg
import time

sg.theme('DarkTeal1')

label_clock = sg.Text('', key='clock')
label = sg.Text('Type in a to-do')
input_box = sg.InputText(tooltip='Enter To-Do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(function.get_todos(), key='list todo', enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
delete_button = sg.Button('Delete', key='delete')
exit_button = sg.Button('Exit', key='exit')

window = sg.Window('My To-Do App',
                   layout=[[label, label_clock],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [delete_button, exit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=950)
    print(event)
    print(values)
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case 'Add':
            if values['todo'] == '':
                continue
            todos = function.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            function.write_todos(todos)
            window['list todo'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['list todo'][0]
                new_todo = values['todo']

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                function.write_todos(todos)
                window['list todo'].update(values=todos)
            except IndexError:
                sg.popup('Please select an item first', text_color='black', font=15)
        case 'list todo':
            updated_input = values['list todo'][0]
            window['todo'].update(value=updated_input.strip())
        case 'delete':
            try:
                todo_to_delete = values['list todo'][0]
                todos = function.get_todos()
                todos.remove(todo_to_delete)
                function.write_todos(todos)
                window['list todo'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Please select an item first', text_color='black', font=15)
        case 'exit':
            break

        case sg.WINDOW_CLOSED:
            break


window.close()



