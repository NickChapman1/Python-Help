## use turtle.write and clear to create the scorebaord at the top
# make a new class that inherts from the turtle class, the scorebaord is a turtle that knows how to track it
#and display it. Track the score and decrement it, or incr. use turtle write and clear and learn on their methods.
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_pos, y_pos)

        self.score_keep()

    def score_keep(self):
        self.clear()
        self.write(f"Score:{self.score}" ,align= "center", font=FONT)#("FONT", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.score_keep()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("courier", 36, "bold"))