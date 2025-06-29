import turtle
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue","yellow","purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    #tim.shape("turtle") Or we can initialize it on set up
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congrationlations You've Won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost- you messed up. {winning_color} turtle took the title..")


        rand_distance = random.randint(0,11)
        turtle.forward(rand_distance)

screen.exitonclick()