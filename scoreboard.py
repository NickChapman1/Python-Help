## use turtle.write and clear to create the scorebaord at the top
# make a new class that inherts from the turtle class, the scorebaord is a turtle that knows how to track it
# and display it. Track the score and decrement it, or incr. use turtle write and clear and learn on their methods.
from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
HIGH_SCORE_FILE = "high_score_snake.txt"
BASE_DIR = "C:/Users/nchapman/PycharmProjects/"

class Scoreboard_snake(Turtle):
    def __init__(self):
        super().__init__()
        self.restart_msg = Turtle()
        self.restart_msg.hideturtle()
        self.restart_msg.penup()
        self.restart_msg.color("white")

        self.start_msg = Turtle()
        self.start_msg.hideturtle()
        self.start_msg.penup()
        self.start_msg.color("white")

        self.running = False
        self.paused = False
        self.started_once = False
        self.score = 0
        self.high_score = self.load_high_score()

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.score_keep()

    def score_keep(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.score_keep()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Courier", 36, "bold"))
        self.save_high_score()
        self.show_restart_screen()
        self.running = False

    def load_high_score(self):
        path = os.path.join(BASE_DIR,HIGH_SCORE_FILE)
        if os.path.exists(path):
            with open(path, "r") as file:
                return int(file.read())
                #file.close() #Not needed because with as manages the file and auto closes basically,
        return 0

    def save_high_score(self):
        path = os.path.join(BASE_DIR,HIGH_SCORE_FILE)
        with open(f"{path}", "w") as file: #"a" wouldve been for append.
            file.write(str(self.high_score))

    def show_restart_screen(self):
        self.restart_msg.clear()
        self.restart_msg.goto(0, -40)
        self.restart_msg.write("Press R to Restart", align="center", font=("Courier", 18, "normal"))

    def show_start_screen(self):
        self.start_msg.clear()
        self.start_msg.goto(0, 0)
        self.start_msg.write("Press SPACE to Start", align="center", font=("Courier", 24, "bold"))

    def start_game(self):
        self.score = 0
        self.running = True
        self.paused = False
        self.started_once = True
        self.score_keep()
        self.start_msg.clear()
        self.restart_msg.clear()

    def restart_game(self):
        self.start_game()

    def pause_game(self):
        if self.running:
            self.paused = not self.paused

    def is_running(self):
        return self.running

    def is_paused(self):
        return self.paused
