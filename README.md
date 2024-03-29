# PysimpleGui
Creating a simple graphical user interface (GUI) that works across multiple platforms can be complicated. But it doesn't have to be that way. You can use Python and the PySimpleGUI package to create nice-looking user interfaces that you and your users will enjoy! PySimpleGUI is a new Python GUI library that has been gaining a lot of interest recently.

<h1 align="left">Installing PySimpleGUI</h1>
<p> PySimpleGUI is a Python package that enables Python programmers of all levels to create GUIs. You specify your GUI window using a "layout" which contains widgets (they're called "Elements" in PySimpleGUI). Regardless of the O.S [Windows,Mac or Linux], on your python interpreter, we will install the package. </P>
<h2 align="left">Open The Command Editor window</h2>
<li> press <strong>win</strong> plus <b>r</b> on your keyboard to open up the shorcut menu bar and type in cmd</li>
<p align ="center"><img src="https://i.imgur.com/NTJ9Pjg.png" /></p>
<li> Run the command <strong>Pip Install PySimpleGUI</strong> </li>

```commandline
Pip install PySimpleGUI
```
<p align ="center"><img src="https://i.imgur.com/PPIknDR.png" /></p>

<h1 align="left">Setting Up Simple Elements</h1>
<p><li>To Create a Window, you should use the following code: </li></p>

```commandline
1. import PySimpleGUI as sg
2. sg.Window(title="Hello Amigo", layout=[[]], margins=(200,100)).read()
```
<p align="left"><img src="https://i.imgur.com/RzKac6z.png" /></p>
<p><li>Run your code to output a window. Depending on the O.S you are using, the window pup ups will differ. </li></p>
<p align="center"><img src="https://i.imgur.com/HCjPeIw.png" /></p>
<p><li>Adding Buttons to the Window</li></p>

```comandline
1. import PySimpleGUI as sg 
2.
3. layout = [
4.	[sg.Text("Hello from silvans")],
5.	[sg.Button("Hi!")]
6.]
7.
8.window = sg.Window("Demo", layout, margins=(200,100))
9.
10.while True:
11.	event, values = window.read()
12.	if event == "Hi!" or event == sg.WIN_CLOSED:
13.		break
14.window.close()
```
<p align="center"><img src="https://i.imgur.com/8vWTyQ0.png" /></p>
<p><li>You can customize the buttons giving them diffrent instructions</li></p>
<p align="center"><img src="https://i.imgur.com/XF9pNkT.png" /></p>


     
