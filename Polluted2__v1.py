# 20200225 multiChoiceGUI_V1.0
"""
*******Change Log*******
V1: set up
************************
"""

# import the library
from appJar import gui

choices = []

class Choices:
    def __init__(self, text, choice1, choice2):
        self.text = text
        self.choice1 = choice1
        self.choice2 = choice2
    
    def displayChoice(self):
        app.setLabel("title", self.text)
        app.setLabel("question1", "1: climb over it")
        app.setLabel("question2", "2: walk around it")


def press(button):
    if button == "Start":
        choices[0].displayChoice()

    if button == "2":
        choices.append(2)
        choiceTwo()

    if button == "Close":
        app.stop()

# choices

choices.append(Choices("you walk towards the mountain","1: climb over it","2: walk around it"))


def choiceOne():
    if choices == [1]:
        app.setLabel("title", "you walk towards the mountain")
        app.setLabel("question1", "1: climb over it")
        app.setLabel("question2", "2: walk around it")
        print (choices)

    if choices == [1, 1]:
        app.setLabel("title", "you reach the top of the mountain and find a cave")
        app.setLabel("question1", "1: walk inside")
        app.setLabel("question2", "2: go down the other side of the mountain")
        print (choices)

    if choices == [2, 1]:
        app.setLabel("title", "You look inside the dumptruck and wow its trash")
        app.setLabel("question1", "1: Pick it up")
        app.setLabel("question2", "2: leave it")
        print (choices)

    if choices == [1, 1, 1]:
        app.setLabel("title", "you walk inside the cave and find corona")
        app.setLabel("question1", "you try and fight but corona gives you a cold")
        app.setLabel("question2", "and then you die")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [2, 1, 1]:
        app.setLabel("title", "")
        app.setLabel("question1", "")
        app.setLabel("question2", "")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [1, 2, 1]:
        app.setLabel("title", "")
        app.setLabel("question1", "")
        app.setLabel("question2", "")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [1, 1, 2, 1]:
            app.setLabel("title", "")
            app.setLabel("question1", "")
            app.setLabel("question2", "")
            app.removeButton("1")
            app.removeButton("2")
            print (choices)


def choiceTwo():
    if choices == [2]:
        app.setLabel("title", "you arrive at the dump truck")
        app.setLabel("question1", "1: look inside")
        app.setLabel("question2", "2: keep walking")
        print (choices)

    if choices == [1, 2]:
        app.setLabel("title", "")
        app.setLabel("question1", "1: ")
        app.setLabel("question2", "2: ")
        print (choices)

    if choices == [2, 2]:
        app.setLabel("title", "as you are walking you find a giant bottle cap stuck in the ground")
        app.setLabel("question1", "you try and lift it and a mutant bottle emerges")
        app.setLabel("question2", "it picks you up and crushes you")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [1, 1, 2]:
        app.setLabel("title", "")
        app.setLabel("question1", "1: ")
        app.setLabel("question2", "2: ")
        print (choices)

    if choices == [2, 1, 2]:
        app.setLabel("title", "littering are you for real, your a monster")
        app.setLabel("question1", "aaaand your dead")
        app.setLabel("question2", "")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [1, 2, 2]:
        app.setLabel("title", "")
        app.setLabel("question1", "")
        app.setLabel("question2", "")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)

    if choices == [1, 1, 2, 2]:
        app.setLabel("title", "")
        app.setLabel("question1", "")
        app.setLabel("question2", "")
        app.removeButton("1")
        app.removeButton("2")
        print (choices)


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
