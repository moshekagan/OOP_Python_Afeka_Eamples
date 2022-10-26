# Example 1 - creation
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Example 2 - access value by key
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict["brand"])       # Ford
print(this_dict.get("brand"))   # Ford

# Example 3 - Dictionaries cannot have two items with the same key:
this_dict = {
  "brand": "Ford",
  "brand": "Mazda",   # Can't use same keys!
  "model": "Mustang",
  "year": 1964
}

# Example 4 - length
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(this_dict))   # 3

# Example 5 - Data types
this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

# Example 6 - get keys
this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(this_dict.keys())   # dict_keys(['brand', 'electric', 'year', 'colors'])


# Example 7 - get values
this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(this_dict.values())   # dict_values(['Ford', False, 1964, ['red', 'white', 'blue']])


# Example 8 - get items
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(this_dict.items())    # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Example 9 - check id key exist
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in this_dict:
  print("Yes, 'model' is one of the keys in the this_dict dictionary")

# Example 10 - change value
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["year"] = 2022
print(this_dict["year"])  # 2022

# Example 11 - update dictionary
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"year": 2022})
print(this_dict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2022}

# Example 12 - add item
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict["color"] = "red"
print(this_dict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Example 13 - Update Dictionary
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
this_dict.update({"color": "red"})
print(this_dict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Example 14 - loop dictionary
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in this_dict:
  print(x)
  # brand
  # model
  # year


# Example 15 - loop dictionary - keys
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in this_dict.keys():
  print(x)
  # brand
  # model
  # year


# Example 16 - loop dictionary - values
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in this_dict.values():
  print(x)
  # Ford
  # Mustang
  # 1964

# Example 17 - loop dictionary - items
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for k, v in this_dict.items():
  print(k, v)
  # brand Ford
  # model Mustang
  # year 1964

# Example 18 - copy
this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
new_dict = this_dict.copy()
print(new_dict)   # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
