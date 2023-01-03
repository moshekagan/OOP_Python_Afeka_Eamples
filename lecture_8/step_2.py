from tkinter import *

window = Tk()
window.title("The best app ever!")

window.geometry("800x600")
lbl = Label(window, text="My Best App", font=("Ariel bold", 50), fg="blue", bg="yellow")
lbl.grid(column=0, row=0)

window.mainloop()
