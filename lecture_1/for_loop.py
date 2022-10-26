# Example 1 - over list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  # apple
  # banana
  # cherry

# Example 2 - over string
for x in "banana":
  print(x)
  # b
  # a
  # n
  # a
  # n
  # a

# Example 3 - break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  # apple
  # banana

# Example 4 - continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  # apple
  # cherry

# Example 4 - over range
for x in range(6):
  print(x)
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5

for x in range(2, 6):
  print(x)
  # 2
  # 3
  # 4
  # 5

for x in range(2, 20, 3):
  print(x)
  # 2
  # 5
  # 8
  # 11
  # 14
  # 17

# Example 5 - pass
for x in [0, 1, 2]:
  pass

# Example 5 - nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana"]

for x in adj:
  for y in fruits:
    print(x, y)
    # red apple
    # red banana
    # big apple
    # big banana
    # tasty apple
    # tasty banana
