import random
import turtle as t
from turtle import Screen

#from turtle import * #Clouds name space and is the worse way to do this 

class Turtlys:
    
    tim = t.Turtle()
    colours = ["tan", "deep pink", "dark magenta", "gold", "light sky blue", "slate gray", "lime"]
    directions = ["forward()", "backward()" ]
    direct = [0,90,180,270]
    
   
    def do_the_turle_walk():
        direct = [0, 90, 180, 270]
        for tur in range(12):
            tim.forward(15)
            tim.setheading(random.choice(direct))
            tim.forward(10)


Screen().exitonclick()