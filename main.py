import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Event Handling")
window.geometry("400x400")

def clickme():
    messagebox.showerror("Error","There is a error")

button=tk.Button(window,text="Click me",command=clickme)
button.pack()

window.mainloop()