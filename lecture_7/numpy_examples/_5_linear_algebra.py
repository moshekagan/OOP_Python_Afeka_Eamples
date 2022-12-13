"""
Linear Algebra
"""

import numpy as np

a = np.ones((2, 3))
print(a)

b = np.full((3, 2), 2)
print(b)

print(np.matmul(a, b))

# Find the Determinant
c = np.identity(3)
print(np.linalg.det(c))


## Reference docs: http://docs.scipy.org/doc/numpy/reference/routines.linalg.html
# Determinant
# Trace
# Singular Vector Decomposition
# Eigenvalues
# Matrix Norm
# Inverse
# Etc...
