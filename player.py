from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):  # add that super class to the call
        super().__init__()  # used to put paddle. can use self. now since its a paddle calss.
        self.shape("turtle")
        self.color("purple")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
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
        self.goto(new_x, new_y)

    def reset_frog(self):
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    ##Wow so this function shown above is the same as below
    # def reached_finish
    #     if self.ycor() > FINISH_LINE_Y
    #         return True
    #     else:
    #         return False