from turtle import Turtle



class Frogs(Turtle):
    def __init__(self, position): #add that super class to the call
        super().__init__() #used to put paddle. can use self. now since its a paddle calss.
        self.shape("turtle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
      # self.position()
  #      self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def go_up(self):  # methods always have a first attribute as self.
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def reset_frog(self):
        self.teleport(0,-1)
        self.move_speed = .1
        self.bounce_x_axis()