from tkinter import *

root = Tk();
root.geometry("500x300+100+100")
root.title("Hi")

name_label = Label(root, text="Name")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)
contact_label = Label(root, text="contact")
contact_label.grid(row=1, column=0)
contact_entry = Entry(root)
contact_entry.grid(row=1, column=1)

gender_label = Label(root, text="Gender")
gender_label.grid(row=2, column=0)
gender = StringVar()
R1 = Radiobutton(root, text="Male", variable=gender, value="Male")
R1.grid(row=3, column=0)
R2 = Radiobutton(root, text="Female", variable=gender, value="Female")
R2.grid(row=3, column=1)
#
interested_label = Label(root, text="Interested In")
interested_label.grid(row=4, column=0)

varC1 = StringVar()
C1 = Checkbutton(root, variable=varC1, onvalue="C", offvalue=0)
C1.grid(row=5, column=0)
varC2 = StringVar()
C2 = Checkbutton(root, variable=varC2, onvalue="C++", offvalue=0)
C2.grid(row=5, column=1)
varC3 = StringVar()
C3 = Checkbutton(root, variable=varC3, onvalue="Java", offvalue=0)
C3.grid(row=5, column=2)
varC4 = StringVar()
C4 = Checkbutton(root, variable=varC4, onvalue="Python", offvalue=0)
C4.grid(row=5, column=3)
#
#
def handleSubmit():
    name = name_entry.get()
    contact = contact_entry.get()
    sex = gender.get()
    interests = f"Interested In {varC1.get()} {varC2.get()} {varC3.get()} {varC4.get()}"
    print(name, contact, sex, interests)


submit = Button(root, text="Submit", command=handleSubmit)
submit.grid(row=6, column=0)
root.mainloop()
