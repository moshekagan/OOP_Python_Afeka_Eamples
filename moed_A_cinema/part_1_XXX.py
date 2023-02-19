from tkinter import *
from tkinter import ttk, messagebox


class Client:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return str(self)


class BookingError(Exception):
    pass


class MovieNotFoundError(Exception):
    pass

"""
Start Area for Question 1
"""
"""
End Area for Question 1
"""


"""
Start Area for Question 2
"""

"""
End Area for Question 2
"""


"""
Start Area for Question 3
"""

"""
End Area for Question 3
"""


# creating instances of the classes
cinema = Cinema("Afeka Cinema")

m_1 = Movie(1, "Shrek", 23, 2, 2023, 17, 90, 2)
m_2 = LimitedMovie(2, "The Godfather", 23, 2, 2023, 19, 175, 4, limit_age=16)
m_3 = Movie(3, "Forrest Gump",  24, 2, 2023, 19, 142, 4)
m_4 = LimitedMovie(4, "Fulp Fiction", 24, 2, 2023, 22, 154, 2, 18)

# adding book to the library
cinema.add_movie(m_1)
cinema.add_movie(m_2)
cinema.add_movie(m_3)
cinema.add_movie(m_4)

# List of members
client_1 = Client("John Smith", 1, 15)
client_2 = Client("Barbara Mary", 2, 20)
client_3 = Client("Robert James", 3, 21)
client_4 = Client("Patricia Roberts", 4, 17)
clients = [client_1, client_2, client_3, client_4]


# helper function that return a chosen client from the Combobox
def get_client_from_combo():
    name = clients_combo.get().split("(")[0].strip()
    for client in clients:
        if client.name == name:
            return client
    return None


# Define a Tkinter GUI Application
window = Tk()
window.title(cinema.name)

window.geometry("750x300")

lbl = Label(window, text=cinema.name, font=("Ariel bold", 40), fg="blue")
lbl.grid(column=0, row=0)

lbl = Label(window, text="Movies list")
lbl.grid(column=0, row=1)

tasks_list = Listbox(window, width=45, height=5)
tasks_list.grid(row=2, column=0)
for m in cinema.movies:
    tasks_list.insert(END, m)
tasks_list["state"] = "disabled"

clients_lbl = Label(window, text="Client")
clients_lbl.grid(row=3, column=1)

clients_combo = ttk.Combobox(window, values=clients)
clients_combo.grid(row=4, column=1)

movie_lbl = Label(window, text="Movie ID")
movie_lbl.grid(row=3, column=2)

movie_entry_txt = Entry(window, width=10)
movie_entry_txt.grid(row=4, column=2)
movie_entry_txt.focus()

"""
Start Area for Question 4
"""
"""
End Area for Question 4
"""

window.mainloop()



