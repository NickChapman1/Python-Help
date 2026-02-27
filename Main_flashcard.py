import os
import random
from tkinter import *
import pandas
import pandas as pd

# Load data
try:
    data = pd.read_csv("data/words_to_learn.csv")
    if data.empty:
        raise ValueError("Empty file")
except (FileNotFoundError, ValueError):
    data = pd.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
words_path = "data/french_words.csv"

data_words = pandas.read_csv("data/french_words.csv")
current_card = {}

def next_card():
    global current_card, flip_timer
    #Cancel the old running flip timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image = card_front_pic)
    #now reset the flip timer
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image = card_back_pic)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn)) #Note the index false
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

def keep_word():
    pd.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)
    next_card()

    #When check is hit remove word from words to learn
    #Make it so try to open words to learn file else french csv
    #If nothing is hit or the x then the word should be appended to words to learn

#______________________________________UI_________________________________________________________
window = Tk()
window.title("FLippy Cards")
window.config(pady=50,padx=50)

flip_timer = window.after(3000, func=flip_card)

#front of card
canvas = Canvas(width=800, height=575, highlightthickness=0)
logo_pic = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 285, image=logo_pic)
canvas.image = logo_pic # <- Line keeps a refrence to tomato
canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column =0, columnspan = 2) #<- Canvas now on grid

#buttons: All these need to be created outside of the functions so they don't die with them.
know_it_pic = PhotoImage(file="images/right.png")
dont_know_pic = PhotoImage(file="images/wrong.png")
card_front_pic = PhotoImage(file="images/card_front.png")
card_back_pic = PhotoImage(file="images/card_back.png")
check_but = Button(image=know_it_pic, highlightthickness=0, command=is_known)
check_but.grid(column =0, row = 1)
x_but = Button(image=dont_know_pic, highlightthickness=0, command=keep_word)
x_but.grid(column =1, row = 1)

# Create text on the canvas
card_background = canvas.create_image(400, 263, image=card_front_pic)

card_title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"), fill="black")
next_card()
window.mainloop()