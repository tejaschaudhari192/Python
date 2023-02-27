from tkinter import *
from tkinter import messagebox
import random
import pyperclip

file_path = "C:/programming/Python/Projects/apps/Password Generator GUI/save_data.txt"

def generate_password():
    letters_small = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letters_cap = [char.upper() for char in letters_small]
    letters_list = letters_small + letters_cap

    numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols_list = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password = (
        [random.choice(letters_list) for letter in range(random.randint(6, 8))]
        + [random.choice(symbols_list) for symbol in range(random.randint(2, 4))]
        + [random.choice(numbers_list) for number in range(random.randint(2, 4))]
    )

    random.shuffle(password)  # random list
    rampass = "".join(password)

    password_input.delete(0, END)
    password_input.insert(END, string=rampass)
    pyperclip.copy(rampass)

def clear():
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)

def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showwarning(title="Bsdk", message=f"Dont Leave any Fields empty")
    else:
        messagebox.askokcancel(
            title="Confirm ?",
            message=f"Website : {website}\nUsername : {username}\nPassword : {password}",
        )

        with open(file_path, "a") as data:
            record = f"{website} || {username} || {password}\n"
            data.write(record)
            clear()


window = Tk()
window.title("Teja's Bandwidth")
# window.minsize(height=1000)
# window.config(pad)

img = PhotoImage(file="C:/programming/100days/Day 29/pass/mylogo_small.png")
canva = Canvas(height=200, width=260)
canva.create_image(133, 100, image=img)
canva.grid(column=1, row=0)

website_note = Label(text="\nWebsite :", font=("arial", 10))
website_note.grid(column=0, row=2)

website_input = Entry(width=40)
# website_input.insert(0, string="www.example.abc")
website_input.grid(column=1, row=2, columnspan=3)
website_input.focus()

username_note = Label(text="\nEmail/Username :", font=("arial", 10))
username_note.grid(column=0, row=3)

username_input = Entry(width=40)
username_input.insert(END, string="address@mail.com")
username_input.grid(column=1, row=3, columnspan=3)

password_note = Label(text="\nPassword :", font=("arial", 10))
password_note.grid(column=0, row=4)

password_input = Entry(width=25)
password_input.grid(column=1, row=4)

gen_pass_btn = Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(column=2, row=4)

submit = Button(command=save, text="Add", width=36, background="white")
submit.grid(column=1, row=5, columnspan=3)

div1 = Label(text="")
div1.grid(column=1, row=6)

exit = Button(command=window.destroy, text="Exit", bg="red", fg="white")
exit.grid(column=1, row=7)

div2 = Label(text="")
div2.grid(column=1, row=8)

window.mainloop()