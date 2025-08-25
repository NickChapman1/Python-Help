from tkinter import *
from tkinter import messagebox
import pandas as pd

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_hit():
    #using .get will get the actual contents rather than the item itself
    website = web_input.get()
    email = email_input.get()
    password = pw_input.get()

    if not website or not email or not password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return
    else:
        messagebox.showwarning(title="Well done", message="Data successfully updated")

    formatted_entry = f"{website} | {email} | {password}\n"
    data_2_capture.append(formatted_entry)
    clear_input()
    save_to_file()
    print(data_2_capture)

def clear_input():
    web_input.delete(0, END)
    email_input.delete(0, END)
    pw_input.delete(0, END)

def save_to_file():#make it output to a text file.
    data_file = pd.DataFrame(data_2_capture)
    data_file.to_csv("passwords.csv", index=False)


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
web_input.grid(column = 1, row = 1, columnspan = 2)
email_input = Entry(width= 35)
email_input.grid(column = 1, row = 2, columnspan = 2)
email_input.insert(0,"fakeemails123@email.gov")
pw_input = Entry(width= 21)
pw_input.grid(column = 1, row = 3)

#buttons:
pw_button = Button(text="Generate Password")
pw_button.grid(column =2, row = 3)
add_button = Button(text="Add", width=36, command=add_button_hit)
add_button.grid(column =1, row = 4, columnspan = 2)








window.mainloop()