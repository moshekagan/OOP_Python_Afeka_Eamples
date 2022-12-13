"""
Basic Mathematics
"""

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([1, 0, 1, 0])
print(a + b)

# Aggregate function
a = np.array([2, 4, 6, 8])
print(a.max())
print(a.min())
print(a.std())
print(a.mean())

# Take the sin / cos
print(np.sin(a))
print(np.cos(a))
