from tkinter import *
from tkinter import ttk

# New Window
window = Tk()
window.title("The best app ever!")
window.geometry("800x600")

# Set Label
lbl = Label(window, text="My Best App", font=("Ariel bold", 50), fg="blue", bg="yellow")
lbl.grid(row=0, column=0)

# Set Entry
entry_txt = Entry(window, width=10)
entry_txt.grid(row=1, column=0)
entry_txt.focus()


# Set Button
def handel_click():
    mood_emoji = ":/"
    mood = mood_combo.get()
    if mood == "Happy":
        mood_emoji = ":)"
    elif mood == "Natural":
        mood_emoji = ":|"
    elif mood == "Sad":
        mood_emoji = ":("

    msg = entry_txt.get()
    if msg == "":
        entry_txt.configure(bg="red")
    else:
        entry_txt.configure(bg="white")
        lbl.configure(text=f"You wrote: {msg} {mood_emoji}")


btn = Button(window, text="Click me!", width=10, height=2, command=handel_click, state="disabled")
btn.grid(row=2, column=0)


# Set Checkbutton
def handel_check():
    if is_check.get() == True:
        btn["state"] = "normal"
    else:
        btn["state"] = "disabled"


is_check = BooleanVar(value=False)
enable_click_checkbox = Checkbutton(window,
                                    text="Enable click",
                                    var=is_check,
                                    command=handel_check)
enable_click_checkbox.grid(row=3, column=0)

# Set Combobox
mood_lbl = Label(window, text="What is your mood?")
mood_lbl.grid(row=4, column=0)

mood_combo = ttk.Combobox(window, values=["Happy", "Natural", "Sad"])
mood_combo.grid(row=4, column=1)

# Set Radiobutton
mood_lbl = Label(window, text="What is your gender?")
mood_lbl.grid(row=5, column=0)

gender_var = StringVar()
gender_values = {
    "Male": "M",
    "Female": "F",
    "Other": "O"
}

current_row = 5
for text, value in gender_values.items():
    r = Radiobutton(window,
                    text=text,
                    value=value,
                    variable=gender_var)
    r.grid(sticky=W, column=1, row=current_row)
    current_row += 1


# Message box
def handel_click_show_gender():
    from tkinter import messagebox
    g = "other"
    if gender_var.get() == "M":
        g = "male"
    elif gender_var.get() == "F":
        g = "female"
    messagebox.showinfo(message=f"Your gender is {g}")


show_gender_btn = Button(window,
                         text="Show gender",
                         width=10,
                         height=2,
                         command=handel_click_show_gender)
show_gender_btn.grid(row=current_row, column=0)
current_row += 1

# Listbox
program_leng = [
    "Python",
    "Perl",
    "C",
    "PHP",
    "JSP",
    "Ruby",
]

def handel_add_js_click():
    program_leng.append("Java Script")

    language_list.delete(0, END)  # clear listbox
    for l in program_leng:  # populate listbox again
        language_list.insert(END, str(l))

language_list = Listbox(window)
for l in program_leng:
    language_list.insert(END, l)
language_list.grid(row=current_row, column=0)

add_js_btn = Button(window,
                    text="Add Java Script",
                    width=20,
                    height=2,
                    command=handel_add_js_click)
add_js_btn.grid(row=current_row, column=1)

# Run App
window.mainloop()
