from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.restart_msg = Turtle()
        self.restart_msg.hideturtle()
        self.restart_msg.penup()
        self.restart_msg.color("black")
        self.level = 1
        self.running = False
        self.paused = False
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_score()
        self.started_once = False

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.running = False
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        self.show_restart_screen()

    def show_restart_screen(self):
        self.restart_msg.clear()
        self.restart_msg.goto(0, -40)
        self.restart_msg.write("Press R to Restart", align="center", font=("Courier", 18, "normal"))
        #return self.restart_msg

    def show_start_screen(self):
        self.start_msg = Turtle()
        self.start_msg.hideturtle()
        self.start_msg.penup()
        self.start_msg.color("black")
        self.start_msg.write("Press SPACE to Start", align="center", font=("Courier", 24, "bold"))

    def start_game(self):
        self.level = 1
        self.running = True
        self.paused = False
        self.started_once = True
        self.update_score()
        if hasattr(self, 'start_msg'):
            self.start_msg.clear()
        if hasattr(self, 'restart_msg'):
            self.restart_msg.clear()

    def restart_game(self):
        self.start_game()
        self.update_score()

    def pause_game(self):
        if self.running:
            self.paused = not self.paused

    def is_running(self):
        return self.running

    def is_paused(self):
        return self.paused

