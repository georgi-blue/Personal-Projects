# This script is running with tkinter
from tkinter import *

# Creating the TKinter object with title name.
root = Tk()
root.title("Georgi's calculator")

# Creating input fields.
inches_e = Entry(root, width=10, borderwidth=5)
weight_e = Entry(root, width=10, borderwidth=5)
miles_e = Entry(root, width=10, borderwidth=5)

# Showing the input fields in the window.
inches_e.grid(row=0, column=1)
weight_e.grid(row=1, column=1)
miles_e.grid(row=2, column=1)


def inches():  # Function to calculate the given centimeters in the input field to inches and show the result.
    centimeters = inches_e.get()
    cm = float(centimeters)
    inches_e.delete(0, END)
    result = cm * 0.393701
    inches_e.insert(0, str(result))


def pounds():  # Function to calculate the given kilograms in the input field to pounds and show the result.
    kilograms = inches_e.get()
    kg = float(kilograms)
    weight_e.delete(0, END)
    result = kg * 2.20462
    weight_e.insert(0, str(result))


def miles():  # Function to calculate the given kilometers in the input field to miles and show the result.
    kilometers = miles_e.get()
    km = float(kilometers)
    miles_e.delete(0, END)
    result = km * 0.621371
    miles_e.insert(0, str(result))


# Creating text labels
my_label1 = Label(root, text='Input centimeters:').grid(row=0, column=0)
my_label2 = Label(root, text='Input kilograms:').grid(row=1, column=0)
my_label3 = Label(root, text='Input kilometers:').grid(row=2, column=0)

# Creating buttons
my_button1 = Button(root, text='Inches!', command=inches)
my_button2 = Button(root, text='Pounds!', command=pounds)
my_button4 = Button(root, text='Miles!', command=miles)

# Showing them in the window
my_button1.grid(row=0, column=2)
my_button2.grid(row=1, column=2)
my_button4.grid(row=2, column=2)

root.mainloop()  # Main Loop for the properly working.
