# Example 1 - create list
example_list = ["apple", "banana", "cherry", "orange", "mango"]
print(example_list)  # ["apple", "banana", "cherry", "orange", "mango"]

# Example 2 - create empty list
empty_list2 = []
print(empty_list2)  # []

# Example 3 - length of a list
example_list = ["apple", "banana", "cherry", "orange", "mango"]
print(len(example_list))    # 5

# Example 4 - Data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Example 4 - list contain different data types
list4 = ["apple", 1, True, ["new list"]]

# Example 5 - Access items
example_list = ["apple", "banana", "cherry", "orange", "mango"]
print(example_list[0])  # apple
print(example_list[1])  # banana

# Example 6 - Negative indexing
example_list = ["apple", "banana", "cherry", "orange", "mango"]
print(example_list[-1])  # mango

empty_list = []
print(empty_list[-1])   # IndexError: list index out of range

# Example 7 - Range of indexes
example_list = ["apple", "banana", "cherry", "orange", "mango"]
print(example_list[2:5])  # ['cherry', 'orange', 'mango']

print(example_list[:4])  # ['apple', 'banana', 'cherry', 'orange']

print(example_list[2:])  # ['cherry', 'orange', 'mango']

# Example 8 - check if item exist
example_list = ["apple", "banana", "cherry", "orange", "mango"]
if "apple" in example_list:
  print("Yes, 'apple' is in the fruits list")

# Example 9 - change item value
example_list = ["apple", "banana", "cherry"]
example_list[1] = "orange"
print(example_list)     # ["apple", "orange", "cherry"]

# Example 10 - insert item to list
example_list = ["apple", "banana", "cherry", "orange"]
example_list.append("mango")
print(example_list)     # ["apple", "banana", "cherry", "orange", "mango"]

# Example 11 - Extend list
list1 = ["apple", "banana"]
list2 = ["cherry", "orange"]
list3 = list1 + list2
print(list3)  # ["apple", "banana", "cherry", "orange"]
