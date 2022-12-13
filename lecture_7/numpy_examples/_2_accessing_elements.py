"""
Accessing / Changing specific elements, row, columns, etc
"""

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print(a.shape)

# get a specific element [row, column]
print(a[1, 5])  # 13

# Get a specific row
print(a[0, :])

# Get a specific column
print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepindex]
print(a[0, 1:6:2])

# Changing item
a[1, 5] = 20
print(a)

a[:, 2] = 5
print(a)

a[:, 3] = [1, 2]
print(a)





