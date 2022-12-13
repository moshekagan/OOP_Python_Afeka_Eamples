"""
Miscellaneous
"""

import numpy as np

# Load data from file

file_data = np.genfromtxt("data.csv", delimiter=",")
print(file_data)
print(file_data.astype("int32"))


# Boolean masking and advanced indexing

print(file_data > 50)

print(file_data[file_data > 50])

print(np.any(file_data > 50, axis=0))

print(np.all(file_data > 50, axis=0))

print(np.all(file_data > 50, axis=1))

## you can index with a list in NumPy

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])


print(((file_data > 50) & (file_data < 100)))
print(~((file_data > 50) & (file_data < 100)))
