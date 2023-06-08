import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text.get("1.0", "end-1c")
    if note:
        with open("notes.txt", "a") as file:
            file.write(note + "\n")
        messagebox.showinfo("Note Saved", "Your note has been saved.")
        text.delete("1.0", "end")

def clear_note():
    text.delete("1.0", "end")

def show_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            messagebox.showinfo("Notes", notes)
    except FileNotFoundError:
        messagebox.showinfo("Notes", "No notes found.")

# Create the main window
window = tk.Tk()
window.title("Notes App")

# Create a text widget for note entry
text = tk.Text(window, height=10, width=50)
text.pack()

# Create buttons for saving, clearing, and displaying notes
save_button = tk.Button(window, text="Save Note", command=save_note)
save_button.pack()

clear_button = tk.Button(window, text="Clear Note", command=clear_note)
clear_button.pack()

show_button = tk.Button(window, text="Show Notes", command=show_notes)
show_button.pack()

# Start the main loop
window.mainloop()
