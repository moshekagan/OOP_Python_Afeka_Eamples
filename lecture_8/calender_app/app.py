from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lecture_8.calender_app.Calendar import Calender
from lecture_8.calender_app.DateTimeError import DateTimeError
from lecture_8.calender_app.Meeting import Meeting
from lecture_8.calender_app.validators import VALID_DAYS, VALID_MONTHS, VALID_YEARS, VALID_DURATION

# Create instance of Calender
calender = Calender()

# New Window
window = Tk()
window.title("Calender")
window.geometry("1000x800")

current_row = 0

# Set Label
lbl = Label(window, text="Book me", font=("Ariel bold", 30), fg="Green")
lbl.grid(row=current_row, column=0)

# status label
status_lbl = Label(window, text="", fg="red")
status_lbl.grid(row=current_row, column=1)

current_row += 1

# Set meeting title
meeting_title_lbl = Label(window, text="Title", fg="blue")
meeting_title_lbl.grid(row=current_row, column=0)
meeting_title_entry = Entry(window, width=20)
meeting_title_entry.grid(row=current_row, column=1)
meeting_title_entry.focus()
current_row += 1

# set date
date_lbl = Label(window, text="Date", fg="blue")
date_lbl.grid(row=current_row, column=0)

day_lbl = Label(window, text="Day")
day_lbl.grid(row=current_row, column=1)
day_combo = ttk.Combobox(window, values=VALID_DAYS)
day_combo.grid(row=current_row+1, column=1)

month_lbl = Label(window, text="Month")
month_lbl.grid(row=current_row, column=2)
month_combo = ttk.Combobox(window, values=VALID_MONTHS)
month_combo.grid(row=current_row+1, column=2)

year_lbl = Label(window, text="Year")
year_lbl.grid(row=current_row, column=3)
year_combo = ttk.Combobox(window, values=VALID_YEARS)
year_combo.grid(row=current_row+1, column=3)

current_row += 2


# set time
time_lbl = Label(window, text="Time", fg="blue")
time_lbl.grid(row=current_row, column=0)

hour_lbl = Label(window, text="Hour")
hour_lbl.grid(row=current_row, column=1)
hour_entry = Entry(window)
hour_entry.grid(row=current_row+1, column=1)

min_lbl = Label(window, text="Minute").grid(row=current_row, column=2)
min_entry = Entry(window)
min_entry.grid(row=current_row+1, column=2)

current_row += 2

# Duration
duration_lbl = Label(window, text="Duration", fg="blue").grid(row=current_row, column=0)
duration_var = IntVar()
for d in VALID_DURATION:
    r = Radiobutton(window,
                    text=f"{d} Minutes",
                    value=d,
                    variable=duration_var)
    r.grid(sticky=W, column=1, row=current_row)
    current_row += 1

# reminder
duration_lbl = Label(window, text="Reminder", fg="blue").grid(row=current_row, column=0)
reminder_checkbox_value = BooleanVar(value=False)
reminder_checkbox = Checkbutton(window,
                                text="Remind me before meeting",
                                var=reminder_checkbox_value)
reminder_checkbox.grid(row=current_row, column=1)
current_row += 1

# Book button
def handel_book_click():
    title = meeting_title_entry.get()
    day = day_combo.get()
    month = month_combo.get()
    year = year_combo.get()
    minute = min_entry.get()
    hour = hour_entry.get()
    duration = duration_var.get()
    reminder = reminder_checkbox_value.get()

    try:
        meeting = calender.creat_new_meeting(title, day, month, year, hour, minute, duration, reminder)
        print("-- all meetings --")
        print(calender.meetings)

        meeting_list.delete(0, END)  # clear listbox
        for m in calender.meetings:  # populate listbox again
            meeting_list.insert(END, str(m))

        status_lbl.configure(text="")
        messagebox.showinfo(message=f"New meeting created!\n {meeting}")
    except (DateTimeError, TypeError) as e:
        print(e)
        status_lbl.configure(text=str(e))


book_btn = Button(window, text="Book", width=10, height=2, command=handel_book_click)
book_btn.grid(row=current_row, column=0)
current_row += 1

# Meeting list
meetings_lbl = Label(window, text="All meetings", fg="blue").grid(row=current_row, column=0)
meeting_list = Listbox(window, width=30)
meeting_list.grid(column=1, row=current_row)
current_row += 1


# Meeting list
def handel_remind_meetings_click():
    remind_meetings_list.delete(0, END)  # clear listbox
    for m in calender.get_all_meeting_to_remind():  # populate listbox again
        remind_meetings_list.insert(END, str(m))


remind_meetings_btn = Button(window, text="Remind me", width=10, height=2, command=handel_remind_meetings_click)
remind_meetings_btn.grid(row=current_row, column=0)

remind_meetings_list = Listbox(window, width=30)
remind_meetings_list.grid(column=1, row=current_row)
current_row += 1

# Run app
window.mainloop()
