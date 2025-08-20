from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER START ------------------------------- #
def button_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER RESET ------------------------------- #
def button_start():
    countdown(WORK_MIN * 60)
    return
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes = count // 60
    seconds = count % 60 # Gets the remainder of seconds
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100, bg=(YELLOW))

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 33))
title_label.grid(column= 1, row=0)

#Tomato picture
canvas = Canvas(width=201, height=225,bg=YELLOW, highlightthickness=0)
Tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=Tomato_pic)
canvas.image = Tomato_pic # <- Line keeps a refrence to tomato
timer_text = canvas.create_text(100, 132, text="00:00",  fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column =1) #<- Canvas now on grid

#My Start button
button = Button(text="Start", command=button_start)
button.grid(column=0, row =2)

#Reset Button
button = Button(text="Reset", command=button_reset)
button.grid(column=2, row =2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,22))
check_marks.grid(row=3, column=1)
#fg=(GREEN),#switch from pack to grid,

window.mainloop()