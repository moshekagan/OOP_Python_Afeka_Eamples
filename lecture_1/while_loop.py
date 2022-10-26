# Example 1
i = 1
while i < 6:
  print(i)
  i += 1
  # 1
  # 2
  # 3
  # 4
  # 5

# Example 2 - break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  # 1
  # 2
  # 3

# Example 3 - continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  # 1
  # 2
  # 4
  # 5
  # 6
