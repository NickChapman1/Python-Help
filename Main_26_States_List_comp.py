import turtle
import pandas

screen = turtle.Screen()
screen.title("US states Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
#wrap it all in a while loop with some condition create the guessed states list
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}Guess States Game",
                                    prompt="Whats another state name").title()
    if answer_state == "Exit":
        # List comprehension really cut this code down, missed states was just an empty list prior.
        missed_states = [m_state for m_state in all_states if m_state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States_to_learn.csv")
        print(f"{missed_states}")
        break



    #if answer is one of the states
    if answer_state in all_states:
        #if they got it right:
            #create a turtle
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        #using the .item() method of the panda series allows us to access only a singular row of data in the panda series, gets the int value
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)

screen.exitonclick()
