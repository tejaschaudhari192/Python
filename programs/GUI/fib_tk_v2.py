from tkinter import *

MEMBERS = """
01 abc
02 xyz
03 xxx
"""
RCPIT = "R C PATEL INSTITUTE OF TECHNOLOGY"
DEPT = "[Department of Electronics & Technology]"


def series_list(num):
    series = []
    a = 1
    b = 0
    for i in range(num):
        c = a + b
        a = b
        b = c
        series.append(a)
    return series


window = Tk()
window.title("Fibonacci Series")
window.config(
    height=400,
    width=400,
)
heading = Label(text="\n" + RCPIT, font=("helvetica", 15))
heading.grid(column=0, row=0)

dept_header = Label(text=DEPT, font=("helvetica", 10))
dept_header.grid(column=0, row=1)

title = Label(text="\nPython Project", font=("helvetica", 15))
title.grid(column=0, row=2)

names = Label(text=MEMBERS, font=("sans serif", 10))
names.grid(column=0, row=3)


SEPARATOR = Label(
    text="-----------------------------------------------------------------------------------"
)
SEPARATOR.grid(column=0, row=4)

# canvas_header = Canvas

enter = Label()
enter.config(text="Enter Kth term : ")
enter.grid(column=0, row=5)

user_input = Entry(width=5)
user_input.config(background="yellow")
user_input.grid(column=0, row=6)

fib_series = Text(
    window, background="skyblue", width=30, height=15, font=("calibri", 12, "bold")
)
fib_series.grid(column=0, row=8)


def show():
    n = user_input.get()
    series = series_list(int(n) + 1)

    fib_series = Text(
        window, background="skyblue", width=30, height=15, font=("calibri", 12, "bold")
    )
    fib_series.grid(column=0, row=8)

    for i in range(1, int(n) + 1):
        fib_series.insert(END, i, "\t", "      ", "\t", series[i])
        fib_series.insert(END, "\n")


gen_btn = Button(text="Generate Series", command=show)
gen_btn.config(background="Green")
gen_btn.grid(column=0, row=7)


exit = Button(command=window.destroy, text="Exit", bg="red", fg="white")
exit.grid(column=0, row=10)
window.mainloop()
