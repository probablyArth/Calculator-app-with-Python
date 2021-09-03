from tkinter import *


root = Tk()
root.title("Calculator app with Python")


inp =Entry(root, width=45, borderwidth=5)
inp.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=20, sticky=EW)


def button_click(num):
    current = inp.get()
    inp.delete(0, END)
    inp.insert(0, f"{str(current)}{str(num)}")

def add():
    global first
    first = int(inp.get())
    inp.delete(0, END)
    second 

# Defining Number Buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Rendering buttons on the screen

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_0.grid(row=5, column=0)

add = Button(root, text="+", padx=35, pady=20)
sub = Button(root, text="-", padx=35, pady=20)
mult = Button(root, text="X", padx=35, pady=20)
equal = Button(root, text="=", padx=35, pady=20)

add.grid(row=2, column=3)
sub.grid(row=3, column=3)
mult.grid(row=4, column=3)
equal.grid(row=5, columnspan=3, column=1, sticky=EW)


root.mainloop()
