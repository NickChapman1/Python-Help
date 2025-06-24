import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
tim.speed(0) # COuld also do fastest this is the same
#pick up pen, move, put down pen draw a circle right five times, up and right five times etc,
#
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    Tuple_test = (r,g,b)
    return Tuple_test

def turn_the_turtle_Left():
    tim.left(90)
    tim.forward(10)
    tim.left(90)
    return

def turn_the_turtle_right():
    tim.right(90)
    tim.forward(10)
    tim.right(90)
    return

def draw_circlesing():
    for _ in range(25):
        tim.pendown()
        tim.color(random_color())
        tim.begin_fill() #fills the circle and needs both begin and end to work.
        tim.circle(5)
        tim.end_fill()
        tim.penup()
        tim.forward(15)
    return

#     tim.left(90)
#     tim.forward(20)
#     tim.left(90)
#     tim.forward(20)
#
#     for _ in range(15):
#         tim.pendown()
#         tim.color(random_color())
#         tim.circle(5)
#         tim.penup()
#         tim.forward(20)
# #
# for _ in range (5):
#     tim.left(90)
#     tim.forward(20)
#     tim.left(90)
#     tim.forward(20)
#     draw_circlesing()
print(tim.xcor())
print(tim.ycor())
# tim.setposition(-200,-200) Instead try teleport to get rid of the line
tim.teleport(-200,-200)
tim.shape("turtle")
#
for _ in range(25):
    draw_circlesing()
    turn_the_turtle_Left()
    draw_circlesing()
    turn_the_turtle_right()



#

screen = t.Screen()
screen.exitonclick()