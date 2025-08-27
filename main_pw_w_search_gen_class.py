from operator import index
from tkinter import *
from tkinter import messagebox #* only imports all the classes
import pandas as pd
from random import choice, randint, shuffle
#import pyperclip
import json

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_creator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #new item for item in range
    password_list = (
        [choice(letters) for _ in range(randint(8, 10))] +
        [choice(symbols) for _ in range(randint(2, 4))] +
        [choice(numbers) for _ in range(randint(2, 4))]
    )

    shuffle(password_list)

    password = "".join(password_list)
    pw_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_hit():
    #using .get will get the actual contents rather than the item itself
    website = web_input.get()
    email = email_input.get()
    password = pw_input.get()
    new_data = {
        website:{ #Has two keys then pass the above defined variables
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                #read the old data
                data = json.load(data_file)
                #update the old data with new

        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            #messagebox.showinfo(title="Success", message="Password saved successfully!")
            clear_input()
###########################Search Functionality*****************************************
def search_pw():
    #test if web input is found
    website_name = web_input.get()
    if len(website_name) == 0:
        messagebox.showwarning(title="Shit", message="Please enter a website to search")
        return
    try:
        with open("data.json", "r") as data_file_captured:
            data = json.load(data_file_captured)
    except(FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website_name in data:
            email = data[website_name]["email"]
            password = data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Not found", message=f"No details for {website_name} found!")



######Input clear##################
def clear_input():
    web_input.delete(0, END)
    email_input.delete(0, END)
    pw_input.delete(0, END)



data_2_capture = []
#new_data = pandas.DataFrame(missed_states)
#new_data.to_csv("States_to_learn.csv")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50,padx=50)
#Logo picture
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.image = logo_pic # <- Line keeps a refrence to tomato
canvas.grid(row = 0, column =1) #<- Canvas now on grid

#Labels:
web_label = Label(text="Website:", fg=GREEN, font=(FONT_NAME, 33))
web_label.grid(column= 0, row=1)
email_label = Label(text="Email/Username:", fg=GREEN, font=(FONT_NAME, 33))
email_label.grid(column= 0, row=2)
pw_label = Label(text="Password:", fg=PINK, font=(FONT_NAME, 33))
pw_label.grid(column= 0, row=3)

#Entries:
web_input = Entry(width= 35)
web_input.grid(column = 1, row = 1)
email_input = Entry(width= 35)
email_input.grid(column = 1, row = 2, columnspan = 2)
email_input.insert(0,"fakeemails123@email.gov")
pw_input = Entry(width= 21)
pw_input.grid(column = 1, row = 3)

#buttons:
pw_button = Button(text="Generate Password", command=password_creator)
pw_button.grid(column =2, row = 3)
add_button = Button(text="Add", width=36, command=add_button_hit)
add_button.grid(column =1, row = 4, columnspan = 2)
search_button = Button(text="Search", width=36, command=search_pw)
search_button.grid(column = 2, row = 1)



window.mainloop()