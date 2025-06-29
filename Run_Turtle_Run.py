import turtle as turtle_module
from turtle import Turtle, Screen
import random

turtle_module.colormode(255)

def get_random_num():
    random_num = random.randint(1, 30)
    print(random_num)
    return random_num

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    Tuple_test = (r,g,b)
    return Tuple_test

def move_forwards():
    timmy.forward(get_random_num())
    tommy.forward(get_random_num())
    terance.forward(get_random_num())
    trevor.forward(get_random_num())
    Terry.forward(get_random_num())
    Tyrone.forward(get_random_num())

timmy = turtle_module.Turtle()
timmy.shape("turtle")
timmy.color(random_color())

tommy = Turtle()#Add the () to make it instantiated.
tommy.shape("circle")
tommy.color(random_color())

Terry = Turtle()
Terry.shape("turtle")
Terry.color(random_color())

terance = Turtle()
terance.shape("square")
terance.color(random_color())

trevor = Turtle()
trevor.shape("classic")
trevor.color(random_color())

Tyrone = Turtle()
Tyrone.shape("triangle")
Tyrone.color(random_color())

terance.right(90)
terance.forward(25)
terance.left(90)

tommy.right(90)
tommy.forward(50)
tommy.left(90)

timmy.right(90)
timmy.forward(75)
timmy.left(90)

Terry.right(90)
Terry.forward(100)
Terry.left(90)

trevor.right(90)
trevor.forward(125)
trevor.left(90)

for _ in range (3):
    move_forwards()

screen = turtle_module.Screen()
screen.exitonclick()
