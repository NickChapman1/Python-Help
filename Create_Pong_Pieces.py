from turtle import Turtle
#from Main import self

class Pong(Turtle):

    def __init__(self, position): #add that super class to the call
        super().__init__() #used to put paddle. can use self. now since its a paddle calss.
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)#errors out when I use teleport for some reason,

    def go_up(self): #methods always have a first attribute as self.
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

