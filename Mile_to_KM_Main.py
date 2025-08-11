#import tkinter
#or
from tkinter import *

def on_button_click():
    kilo_base = 1.6
    try:
        miles_ran = float(miles_input.get())
        KM = miles_ran * kilo_base
        label_for_km_num.config(text=f"{KM}")
    except ValueError:
        label_for_km_num.config(text="Invalid Input")



window = Tk()
window.title("My First Screen Play: Miles to Kilometer Converter")
window.minsize(width=300, height=150)
#use pad iwthin .config of a widget to change the padding around the box.
window.config(padx=15,pady=15)

#label for miles
my_label = Label(text="Miles", font=("Arial", 24, "bold"))
my_label.grid(column=4, row= 1)

#entry for Miles
miles_input = Entry(width=10)
print(miles_input.get())
miles_input.grid(column =2, row =1)

#label for Km
label_for_km = Label(text="Km", font=("Arial", 24, "bold"))
label_for_km.grid(column=4, row= 2)

#Entry for Km switching this to just a text label that gets replaced
label_for_km_num = Label(text="0", font=("Arial", 24, "bold"))
label_for_km_num.grid(column=3, row= 2)

#label for is equal
label_for_km = Label(text="Is Equal to:", font=("Arial", 24, "bold"))
label_for_km.grid(column=0, row= 2)

#Calculate button
button = Button(text="Calculate", command=on_button_click)
button.grid(column=2, row =3)



window.mainloop()