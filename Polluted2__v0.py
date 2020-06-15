"""
*******Change Log*******
V1: set up
************************
"""

# import the library
from appJar import gui

def press(button):
    if button == "Start":
        choices[0].displayChoice()

    if button == "2":
        choices.append(2)
        choiceTwo()

    if button == "Close":
        app.stop()

# create a GUI variable called app
app = gui("Login Window", "1250x500")
app.setBg("grey")
app.setFont(30)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to Polluted Two, 1 or 2")
app.setLabelBg("title", "green")
app.setLabelFg("title", "black")

app.addLabel("question1", "")
app.addLabel("question2", "")
app.setLabelFg(["question1", "question2"], "white")

# link the buttons to the function called press
app.addButtons(["1", "2"], press)
app.setButton("1","Start")
app.addButton("Close", press)
app.setButtonWidth(["1", "2"], 10)

# start the GUI
app.go()
