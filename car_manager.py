from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#create all the cars and move them accross the screen,.

class Cars_build(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=random.randint(1,3))
        self.penup()
        self.goto(300, random.randint(-250, 250))
        self.setheading(180)  # Move left
        self.speed("fastest")
        self.random_x = random.randint(0,50)
        self.y_move = 10
        self.x_move = 10

    def move(self, speed):
        self.forward(speed)
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor()
        # # new_y = self.ycor() + self.y_move
        # self.goto(new_x,new_y)

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Cars_build()
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.move(self.car_speed)

    def increase_speed(self):
        self.car_speed += 2