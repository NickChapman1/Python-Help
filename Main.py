from turtle import Turtle, Screen
import random

timmy = Turtle()
tommy = Turtle() #Add the () to make it instantiated.
screen = Screen()


def move_forwards():
    timmy.forward(10)

def move_back():
    timmy.back(10)

def counter_the_clock():
    timmy.left(15)
    #Or you could do this, same difference.
    # new_heading = timmy.heading() + 10
    # timmy.setheading(new_heading)

def clock_wise_gamgi():
    timmy.right(15)

def shake_it_up():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key = "w", fun=move_forwards) #I geuss when passing functions as parameters you leave out ()
#Or it will be messed up and not call right. Calculator is a great example of when 2 use function into function
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_the_clock)
screen.onkey(key="d", fun=clock_wise_gamgi)
screen.onkey(key="c", fun=shake_it_up)




screen.exitonclick()
