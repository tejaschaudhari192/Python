import json
from tkinter import *
from tkinter import messagebox

file_path = "C:/programming/Python/programs/GUI/notes.json"

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
        title = note_title.get()
        note = new_note.get("1.0", "end-1c")
        new ={
            title : {
            'id': id,
            'note': note
        }
        }
        notes_list.append(new)
        print(notes_list)
        all()
        if len(title) == 0 or len(note) == 0 :
            messagebox.showwarning(title="Bsdk", message=f"Dont Leave any Fields empty")
        else:
            messagebox.askokcancel(
                title="Confirm ?",
                message=f"Website : {title}\nUsername : {note}",
            )
            try:
                with open(file_path, "r") as data:
                    curr_data = json.load(data)

            except FileNotFoundError:
                with open(file_path, "w") as data:
                    json.dump(new, data, indent=4)
            else:    
                curr_data.update(new)
                with open(file_path, "w") as data:
                    json.dump(curr_data, data, indent=4)
            finally:
                pass
                clear()
    
    add_btn = Button(text='Add', command=add)
    add_btn.grid(column=1,row=0)
newNote()

def viewNote(note):
    tit = note['title']
    messagebox.askokcancel(title=tit,message=note['note'])
# global pos 
# pos = 0
def all():
    for note in notes_list:
        # pos += 1
        def vn(note=note):
            viewNote(note)
        id = note["id"]
        note_btn = Button(text=f'view note {id}',command=vn,)
        note_btn.grid(column=0,row=note['id']+1)
all()
window.mainloop()