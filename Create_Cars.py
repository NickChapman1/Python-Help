from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self, y_cordinate):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(0,y=y_cordinate)
        self.random_x = random.randint(0,50)
        self.y_move = 10
        self.x_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor()
        # new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

