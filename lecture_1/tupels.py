# Example 1 - creation
thistuple = ("apple", "banana", "cherry")
print(thistuple)    # ('apple', 'banana', 'cherry')

# Example 2 - length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))    # 3

# Example 3 - Data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Example 4 - tuples contain different data types
tuple4 = ("abc", 34, True, 40, "male")

# Example 5 - access item
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Example 6 - negative indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Example 7 - range of indexing
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[2:])

# Example 8 - check if exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# We can't update Tuples! We can convert it to list and then update and convert to tuple

# Example 9 - convert to list
this_tuple = ("apple", "banana", "cherry")
this_list = list(this_tuple)
print(this_list)    # ["apple", "banana", "cherry"]

# Example 10 - convert list to tuple
this_list = ["apple", "banana", "cherry"]
this_tuple = tuple(this_list)
print(this_tuple)    # ("apple", "banana", "cherry")



