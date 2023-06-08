from tkinter import *
from tkinter import messagebox
window  = Tk()
window.title('Teja\'s Notes')
window.configure(background='black')

notes_list = [{
    'id': 1,
    'title': 'none',
     'note' : 'sample note'
}]
# pos = 0
# global id
id = 1


def newNote():
    note_title = Entry()
    note_title.insert(0, 'title')
    note_title.grid(column=0,row=0)
    new_note = Text(window, height=10, width=50)
    new_note.insert(END,chars='description')
    new_note.grid(column=0,row=1)
    # note_id = id + 1
    # pos += 1
    
    def add():
        global id
        id += 1
        if len(note_title.get()) == 0 or len(new_note.get("1.0", "end-1c")) == 0 :
            messagebox.showwarning(title="Bsdk", message=f"Dont Leave any Fields empty")
            
        else:
            note = {
                'id': id,
                'title': note_title.get(),
                'note': new_note.get("1.0", "end-1c")
            }
            notes_list.append(note)
            print(notes_list)
            all()
    
    add_btn = Button(text='Add', command=add)
    add_btn.grid(column=1,row=0)
newNote()

def viewNote(note):
    messagebox.askokcancel(title=note['title'],message=note['note'])
# global pos 
# pos = 0
def all():
    for note in notes_list:
        # pos += 1
        def vn(note=note):
            viewNote(note)
        # id = note['id']
        note_btn = Button(text=f'view note {note["title"]}',command=vn,)
        note_btn.grid(column=0,row=note['id']+1)
all()
window.mainloop()