# 20200225 multiChoiceGUI_V1.0
"""
*******Change Log*******
V1: set up
************************
"""

# import the library
from appJar import gui

choices = []
roundCounter = 0

class Choices:
    def __init__(self, text, choice1, choice2):
        self.text = text
        self.choice1 = choice1
        self.choice2 = choice2
    
    def displayChoice(self):
        app.removeAllWidgets()
        app.addLabel("title", self.text)
        app.addButton(self.choice1,press)
        app.addButton(self.choice2,press)


def press(button):
    global roundCounter
    if button == "Start":
        choices[0].displayChoice()
    if button == "1: climb over it":
        app.removeAllWidgets()
        app.addLabel("title","you reach the top of the mountain and find a cave")
    if button == "2: walk around it":
        app.setLabel("title","As you are walking you run into a plastic bag")
   
    if button == "Close":
        app.stop()        

# choices

choices.append(Choices("you walk towards the mountain","1: climb over it","2: walk around it"))
"""
def press(button):
    global roundCounter
    if button == "1: climb over it":
        choices[0].displayChoice()
    if button == "1: walk inside":
        app.setLabel("title","you walk inside the cave and find corona")
    if button == "2: go down the other side of the mountain":
        app.setLabel("title","As you are walking you run into a plastic bag")
   
    if button == "Close":
        app.stop()        

# choices

choices.append(Choices("you reach the top of the mountain and find a cave","1:  walk inside","2: go down the other side of the mountain"))
"""

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
app.addButton("Start",press)

# start the GUI
app.go()
