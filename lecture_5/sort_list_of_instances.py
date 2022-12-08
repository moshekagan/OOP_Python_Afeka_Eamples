# """
#     Sort list of instances
# """

ls = ["Cherry", "Apple", "Blueberry"]

print(sorted(ls))

# sorted by len
print(sorted(ls, key=len))

# alternative form using lambda
print(sorted(ls, key=lambda x: len(x)))


# example of sorting instances of Fruit class by price

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price


L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

for f in sorted(L, key=lambda x: x.price):
    print(f.name)


# another way : using a method

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


L = [Fruit("Cherry", 10), Fruit("Apple", 5), Fruit("Blueberry", 20)]

# sorted by price, referencing a class method
for f in sorted(L, key=Fruit.sort_priority):
    print(f.name)

# another way to do the same thing
for f in sorted(L, key=lambda x: x.sort_priority()):
    print(f.name)
