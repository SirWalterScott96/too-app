import function
import PySimpleGUI as Ps

label = Ps.Text('Type in a to-do')
input_box = Ps.InputText(tooltip='Enter To-Do')
add_button = Ps.Button('Add')

window = Ps.Window('My To-Do App', layout=[[label], [input_box, add_button]])

window.read()

window.close()



