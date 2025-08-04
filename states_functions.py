import turtle
import pandas as pd

class States:
    def __init__(self, image_file, csv_file):
        self.screen = turtle.Screen()
        self.screen.title("U.S States Game")
        self.screen.setup(width=725, height=491)
        self.screen.bgpic("blank_states_img.gif")

        self.data = pd.read_csv(csv_file)
        self.states_dict = {
            row.state: (row.x, row.y) for _, row in self.data.iterrows()
        }

    def mark_state(self, name):
        if name in self.states_dict:
            x, y = self.states_dict[name]
            marker = turtle.Turtle()
            marker.hideturtle()
            marker.penup()
            marker.goto(x, y)
            marker.write(name, align="center", font=("Arial", 10, "normal"))
            return True
        return False