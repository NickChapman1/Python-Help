from turtle import Turtle
from Create_Pong_Pieces import Pong


class Balls(Turtle):
    def __init__(self, position): #add that super class to the call
        super().__init__() #used to put paddle. can use self. now since its a paddle calss.
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10
       # self.goto(position)#errors out when I use teleport for some reason,
        # is_on_screen = True
        # while is_on_screen:
        #     self.forward(10)
        # if self == position(r_paddle or l_paddle):
        #     self.setheading(+180)
        #     self.forward(10)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y_axis(self):
        self.y_move *= -1

    def bounce_x_axis(self):
        self.x_move *= -1
        self.move_speed *= .9

    # def increase_ball_speed(self):
    #     self.move_speed -= .01

    def reset_ball(self):
        self.teleport(0,0)
        self.move_speed = .1
        self.bounce_x_axis()