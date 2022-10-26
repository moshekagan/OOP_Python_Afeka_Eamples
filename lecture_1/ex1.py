import random


def choose_item_from_list(items):
    len_of_items = len(items)
    chosen_index = random.randint(0, len_of_items)

    return items[chosen_index]


students = []

for i in range(5):
    name = input("insert a name: ")
    students.append(name)

winner_student = choose_item_from_list(students)

print(f"The winner student is: {winner_student}! :)")
