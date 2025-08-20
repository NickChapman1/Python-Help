import math
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
reps = 0
timer = None

# ---------------------------- TIMER START ------------------------------- #
def button_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER RESET ------------------------------- #
def button_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec= SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text ="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text="Shorter Break", fg=PINK)
    else:
        countdown(work_sec)
        title_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        button_start()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)
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
canvas.grid(row = 1, column =1) #<- Canvas now  on grid

#My Start button
button = Button(text="Start", command=button_start)
button.grid(column=0, row =2)

#Reset Button
r_button = Button(text="Reset", command=button_reset)
r_button.grid(column=2, row =2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME,22))
check_marks.grid(row=3, column=1)
#fg=(GREEN),#switch from pack to grid,

window.mainloop()