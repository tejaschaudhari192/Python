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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global REPS
    window.after_cancel(timer)
    canva.itemconfig(timer_style, text="00:00")
    tick_mar["text"] = ""
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    if REPS % 2 is 1:
        coundown(WORK_MIN * 60)
        heading.config(text="Work", fg=GREEN)
    elif REPS is 8:
        coundown(LONG_BREAK_MIN * 60)
        heading.config(text="Break", fg=RED)
    else:
        coundown(SHORT_BREAK_MIN * 60)
        heading.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def coundown(count):
    global timer
    min = count // 60
    sec = count % 60
    if min < 10:
        min = f"0{min}"
    if sec < 10:
        sec = f"0{sec}"

    canva.itemconfig(timer_style, text=f"{min}:{sec}")
    if count > 0:
        timer = window.after(1000, coundown, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(REPS // 2):
            mark += "✔"
        tick_mar["text"] = mark


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Teja's Timer")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)

canva = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="C:/programming/100days/Day 28/pomodoro/tomato.png")
canva.create_image(100, 112, image=img)
timer_style = canva.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold")
)
canva.grid(column=1, row=1)

heading = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
heading.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

tick_mar = Label(text="", font=(20,), fg=GREEN, bg=YELLOW)
tick_mar.grid(column=1, row=3)

exit_button = Button(command=window.destroy, text="Exit", bg="red", fg="white")
exit_button.grid(column=1, row=4)

window.mainloop()