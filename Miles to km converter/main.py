from tkinter import *

window = Tk()
window.title("Mile to Km conversion")
window.minsize(width=100, height=100)
window.config(padx=100, pady=100)

def calculate():
    miles = float(input.get())
    km = round(miles * 1.61)
    Kilometer_result_label.config(text=km)

label = Label(text="Enter",font=('Arial',15,"bold"))
label.grid(column=0, row=0)
label.config(padx=20,pady=20)

input = Entry(width=10)
input.get()
input.grid(column=1,row=0)


miles_label = Label(text= "Miles",font=('Arial',15,"bold"))
miles_label.grid(column=2,row=0)
miles_label.config(padx=20, pady=0)

is_equal_to_label = Label(text ="is equal to", font=('Arial', 15, "bold"))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=20, pady=20)

kilometer_label = Label(text ="Kilometer", font=('Arial', 15, "bold"))
kilometer_label.grid(column=2, row=1)
kilometer_label.config(padx=20, pady=20)

Kilometer_result_label = Label(text=0, font=('Arial', 15, "bold"))
Kilometer_result_label.grid(column=1, row = 1)
Kilometer_result_label.config(padx=20, pady=20)



button = Button(text="Calculate",font=('Arial',15,"bold"),command = calculate)
button.grid(column=1,row=3)










window.mainloop()
