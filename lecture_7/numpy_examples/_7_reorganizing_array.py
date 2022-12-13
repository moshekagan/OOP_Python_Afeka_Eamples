"""
Reorganizing array
"""

import numpy as np

before = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8]])
print(before)
print(before.shape)


after = before.reshape((8, 1))
print(after)

after = before.reshape((4, 2))
print(after)

try:
    after = before.reshape((3, 2))
    print(after)
except ValueError:
    print("It's not fit!")


# Vertical stacking vectors
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

print(np.vstack((v1, v2)))
print(np.vstack([v1, v2, v1, v2]))

# Horizontal stacking vectors
h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

print(np.hstack((h1, h2)))


