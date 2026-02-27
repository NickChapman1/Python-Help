from states_functions import States

#initalize game
game = States("blank_states_img.gif", "50_states.csv")
#Set up an empty dictionary
guessed_states = []

while len(guessed_states) < 50:
    answer = game.screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"

    )

    if answer is None:
        print("Not valid")
        break

#Makes it so all input is lowercase minus the starting letters, so format will match
    # and strip removes trailing and leading spaces.
    answer = answer.strip().title()

    if answer not in guessed_states and game.mark_state(name=answer):
        guessed_states.append(answer)

game.screen.mainloop()