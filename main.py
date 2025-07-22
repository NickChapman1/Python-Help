import time
from turtle import Turtle
from random import random, randint
from turtle import Screen
from player import Player
from car_manager import CarManager, Cars_build
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
frog_1 = Player()
score_frog = Scoreboard()
#car_creator = Cars_build()

start_msg = score_frog.show_start_screen() #this shows the start screen

# Key bindings Key bindings are part of the input system, and main.py
# is where the game is orchestrated — so it’s the right place to wire up input to behavior.
def handle_start():
    global start_msg
    if not score_frog.started_once:
        score_frog.start_game()
        frog_1.reset_frog()
        car_manager.reset()
        # if start_msg:
        #     start_msg.clear()

def handle_restart():
    if score_frog.started_once and not score_frog.is_running():
        score_frog.restart_game()
        frog_1.reset_frog()
        car_manager.reset()

def handle_pause():
    score_frog.pause_game()

screen.listen()
screen.onkey(frog_1.go_up, "Up")
#screen.onkey(frog_1.go_down, "Down") #leaving just up functionality for now
screen.onkey(handle_start, "space")
screen.onkey(handle_restart, "r")
screen.onkey(handle_pause, "p")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)

    if not score_frog.is_running() or score_frog.is_paused():
        continue

    car_manager.create_car()
    car_manager.move_cars()

    #COllisions checking
    for car in car_manager.all_cars:
        if car.distance(frog_1) < 20:
            score_frog.game_over()
            score_frog.show_restart_screen()
            break
            #game_is_on = False
    #detect finish line
    if frog_1.reached_finish_line():
        frog_1.reset_frog()
        car_manager.increase_speed()
        score_frog.increase_level()
        #score_frog.update_score()# this gets hit with the call to increase level

screen.exitonclick()
    # if frog_1.distance() < 15:
    #     print("GG GAMEOVER")
    #     game_is_on = False