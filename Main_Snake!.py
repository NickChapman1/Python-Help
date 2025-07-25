import random
import turtle
import time
from scoreboard import Scoreboard_snake
from snake import Snake
from food import Food ## Okay so what comes after the from can be the file you're pulling where the other thing exists
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_keeper = Scoreboard_snake()


game_is_on = False  # Start with game off

def play_game():
    global game_is_on
    game_is_on = True
    score_keeper.start_game()
    snake.reset_snake()
    food.refresh()

    # Countdown before game starts
    countdown = Turtle()
    countdown.hideturtle()
    countdown.color("white")
    countdown.penup()
    countdown.goto(0, 0)
    for num in ["3", "2", "1", "GO!"]:
        countdown.write(num, align="center", font=("Courier", 48, "bold"))
        screen.update()
        time.sleep(1 if num != "GO!" else 0.5)
        countdown.clear()

    while game_is_on:
        screen.update()
        time.sleep(.1)

        if not score_keeper.is_running() or score_keeper.is_paused():
            continue

        snake.move()
    ##detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_keeper.increase_score()
            score_keeper.score_keep()
            print("nom nom nom")
        # check if the snake stays in screen.
        if (snake.head.xcor() > 288 or snake.head.xcor() < -288
                or snake.head.ycor() > 288 or snake.head.ycor() < -288):
            game_is_on = False
            score_keeper.game_over()

        # detect colision with the wall

        #     #distnace function takes a parameter of what you're trying to see how far from you are
        #     if segment == snake.head:
        #         pass
        for segment in snake.segments[1:]:  # Gives us everything but the first. Power of splicing right here.
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score_keeper.game_over()
# Key bindings Key bindings are part of the input system, and main.py
# is where the game is orchestrated — so it’s the right place to wire up input to behavior.
def handle_start():
    if not score_keeper.started_once:
        play_game()

def handle_restart():
    if score_keeper.started_once and not score_keeper.is_running():
        play_game()

def handle_pause():
    score_keeper.pause_game()

#keybindings
screen.listen()
screen.onkey(handle_start, "space")
screen.onkey(handle_restart, "r")
screen.onkey(handle_pause, "p")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")
screen.onkey(snake.left, key="Left")

score_keeper.show_start_screen()
screen.mainloop()
