from tkinter import *
from tkinter import ttk

window = Tk()
window.title("The best app ever!")

window.geometry("800x600")

lbl = Label(window, text="My Best App", font=("Ariel bold", 50), fg="blue", bg="yellow")
lbl.grid(column=0, row=0)

entry_txt = Entry(window, width=10)
entry_txt.grid(column=0, row=1)
entry_txt.focus()


def handel_click():
    msg = entry_txt.get()
    if msg == "":
        entry_txt.configure(bg="red")
    else:
        entry_txt.configure(bg="white")
        lbl.configure(text=f"You wrote: {msg}")


btn = Button(window, text="Click me!", width=10, height=2, command=handel_click)
btn.grid(column=0, row=2)


window.mainloop()
