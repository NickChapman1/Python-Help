from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20,0), (-40,0)] #Constants are all caps and snake case using _
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        #for _ in range (4):
        new_snake_piece = Turtle("square")
        new_snake_piece.color("grey")
        new_snake_piece.penup()
        new_snake_piece.goto(position)
        self.segments.append(new_snake_piece)

    def extend(self):
        self.add_segment(self.segments[-1].position()) ##position is a method from the turtle class,
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # range function comes from C Parameters are start stop step
            new_x = self.segments[seg_num - 1].xcor()  # segment 2 - 1 gets you to the middle segment
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP: #makes it so it can't move backwards.
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            
    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move off-screen before clearing
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

