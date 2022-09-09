import PySimpleGUI as sg 

layout = [
	[sg.Text("Hello from silvans")],
	[sg.Button("Hi!")]
]

window = sg.Window("Demo", layout, margins=(200,100))

while True:
	event, values = window.read()
	if event == "Hi!" or event == sg.WIN_CLOSED:
		break
window.close()
