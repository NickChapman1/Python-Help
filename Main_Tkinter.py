#import tkinter
#or
from tkinter import *

button_clicked = False

def on_button_click():
    global button_clicked
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First Screen Play")
window.minsize(width=500, height=300)
#use pad iwthin .config of a widget to change the padding around the box.
window.config(padx=15,pady=15)

#label
my_label = Label(text="I am label", font=("Arial", 24, "bold"))
my_label.config(text="new Text")
my_label.grid(column=0, row= 0)

#button
button = Button(text="click me", command=on_button_click)
button.grid(column=1, row =1)

new_button = Button(text="New_button identified")
new_button.grid(column=2, row=0)

#entry
input = Entry(width=8)
print(input.get())
input.grid(column = 3, row =2)







window.mainloop()