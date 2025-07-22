from turtle import Turtle, Screen
from Frog_man import Frogs
from Create_Cars import Cars
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("Grey")
screen.title("FROGGER")
game_is_on = True
car_1 = Cars(y_cordinate=-100)
car_2 = Cars(y_cordinate=-50)
car_3 = Cars(y_cordinate=-150)

frog_1 = Frogs(1)
screen.listen()
screen.onkey(frog_1.go_up, "Up")
screen.onkey(frog_1.go_down, "Down")


while game_is_on:
    car_1.move()
    car_3.move()

#Make a frog object



#Make car objects that move

# randomize the car genenaration and how the objects move in each lane

#build road objects out of stationary snake objects just loop it?

#Make it so its game over if frog touches random objects.

screen.exitonclick()