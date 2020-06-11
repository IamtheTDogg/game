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
    def __init__(self, text, choice1, choice2, aGoes, bGoes):
        self.text = text
        self.choice1 = choice1
        self.choice2 = choice2
        self.aGoes = aGoes
        self.bGoes = bGoes
    
    def displayChoice(self):
        app.removeAllWidgets()
        app.addLabel("title", self.text)
        app.addButton("A",press)
        app.setButton("A",self.choice1)
        app.addButton("B",press)
        app.setButton("B",self.choice2)


def press(button): 
    global roundCounter
    if button == "Start":
        choices[0].displayChoice()
        
    if button == "A":
        choices[choices[roundCounter].aGoes].displayChoice()
        roundCounter = choices[roundCounter].aGoes
        
    if button == "B":
        choices[choices[roundCounter].bGoes].displayChoice()
        roundCounter = choices[roundCounter].bGoes
        
    if button == "Close":
        app.stop()        

# choices

choices.append(Choices("you walk towards the mountain","1: climb over it","2: walk around it",1,6))
choices.append(Choices("you reach the top of the mountain and find a cave","1:  walk inside","2: go down the other side of the mountain",2,9))
choices.append(Choices("you walk into the cave and find corona fight or run","1: fight","2: run",3,10))
choices.append(Choices("you try to fight corona but corona gives you a cold what do you do","1: live out your last days","2: keep fighting",4,11))
choices.append(Choices("you find a nice trash cottage live there or keep moving","1: live there","2: keep moving",5,13))
choices.append(Choices("as you are dying you play animal crossing to die happily","1: restart","2: restart",0,0))
choices.append(Choices("you walk around it and find a hobo trying to sell shrooms","1: buy them","2: keep going",7,16))
choices.append(Choices("you buy the shrooms and he tells you not to take all of them at once","1: take them all at once","2: listen to him",8,21))
choices.append(Choices("you take all of them have two secounds of fun then your brain explodes","1: restart","2: restart",0,0))
choices.append(Choices("you slip and fall to your death","1: restart","2: restart",0,0))
choices.append(Choices("you try to run but corona throws its bottle cap at you and you get beheaded","1: restart","2: restart",0,0))
choices.append(Choices("you keep fighting and beat corona virus by picking up a pot lid and covering your face and beat the game","1: continue","2: restart",12,0))
choices.append(Choices("why did you continue you already won you idiot","1: restart","2: restart",0,0))
choices.append(Choices("you continue on your journey and find a man selling apples ","1: buy an apple","2: continue walking",14,16))
choices.append(Choices("you buy the apple and eat it and after you eat it the man says it cures corona virus","1: continue walking","2: steal more apples",16,15))
choices.append(Choices("you try to steal the apples but the man stabs you","1: restart","2: restart",0,0))
choices.append(Choices("you continue walking until you find a church","1: walk in ","2: continue walking",17,20))
choices.append(Choices("you walk in and find jesus just chilling there","1: ask whats up","2: leave",18,20))
choices.append(Choices("jesus says not much wanna go to heaven","1: yea","2: nah",19 ,20))
choices.append(Choices("you say sure and jesus pulls a revolver out and kills you","1: restart","2: restart",0,0))
choices.append(Choices("you continue walking into the sunset and die from lack of water","1: restart","2: restart",0,0))
choices.append(Choices("you try the shrooms and end up having a bad trip and you pull out your eyes dont do drugs","1: restart","2: restart",0,0))

# create a GUI variable called app
app = gui("Login Window", "1900x800")
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
