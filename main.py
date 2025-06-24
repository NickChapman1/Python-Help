#import Turtle_Methods
#from Turtle_Methods import Turtlys
#The turtle module will be know as t
import turtle as t
import random
import colorgram


#New_Turtlys = Turtle_Methods.Turtlys
colors = colorgram.extract('image.jpg', 6)
first_color = colors[0]
rgb = first_color.rgb
hsl = first_color.hsl
proportion = first_color.proportion

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    Tuple_test = (r,g,b)
    return Tuple_test

colours = ["tan", "deep pink", "dark magenta", "gold", "light sky blue", "slate gray", "lime"]
directions = [0, 90, 180, 270]
test_variable = 1

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        # tim.color(colors) #use with colorgram library
        tim.color(random_color())
        tim.circle(10)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()