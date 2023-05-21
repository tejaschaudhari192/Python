from tkinter import *


def fib(k):
    if k <= 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


def series_list(user_input):
    num = int(user_input) + 1
    if num == 1:
        series = [0]
    else:
        series = [fib(i) for i in range(0, num - 1)]
        series = [0] + series
    return series


window = Tk()
window.title("Fibonacci Series")
window.config(
    height=50,
    width=60,
)

enter = Label()
enter.config(text="Enter Kth : ")
enter.grid(column=0, row=0)

user_input = Entry(width=5)
user_input.config(background="yellow")
user_input.grid(column=0, row=1)

fib_series = Text(
    window, background="skyblue", width=30, height=15, font=("calibri", 12, "bold")
)
fib_series.grid(column=0, row=3)


def show():
    n = user_input.get()
    series = series_list(n)
    
    if int(n) > 35:
        Message.mess.showwarning(title="pc says", message=f"tmkc")

    fib_series = Text(
        window, background="skyblue", width=30, height=15, font=("calibri", 12, "bold")
    )
    fib_series.grid(column=0, row=3)

    for i in range(1, int(n) + 1):
        fib_series.insert(END, i, "\t", "      ", "\t", series[i])
        fib_series.insert(END, "\n")


gen_btn = Button(text="Generate Series", command=show)
gen_btn.config(background="Green")
gen_btn.grid(column=0, row=2)


exit = Button(command=window.destroy, text="Exit", bg="red", fg="white")
exit.grid(column=0, row=5)
window.mainloop()
