def reader():
    label.config(text=sc.get())


from tkinter import *

root = Tk();
root.geometry("500x300+100+100")
root.title("Hi")

sc=Entry(root)
sc.pack()


label = Label(root,text="level")
label.pack()

def selec():
    label.config(text="option"+str(op.get()));


op=IntVar()
o1 = Radiobutton(root,text="One",value=1,variable=op)
o1.pack()
o2 = Radiobutton(root,text="Two",value=2,variable=op)
o2.pack()
o3 = Radiobutton(root,text="Two",value=3,variable=op)
o3.pack()

btn=Button(root,text="op",command=selec)
btn.pack()



root.mainloop()