from tkinter import *

window = Tk()
window.title("The best app ever!")

window.geometry("800x600")
lbl = Label(window, text="My Best App", font=("Ariel bold", 50), fg="blue", bg="yellow")
lbl.grid(column=0, row=0)


def handel_click():
    lbl.configure(text=f"You just clicked on me!")


btn = Button(window, text="Click me!", width=10, height=2, command=handel_click)
btn.grid(column=0, row=1)

window.mainloop()
