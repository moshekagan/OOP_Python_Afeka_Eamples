"""
ndarray vs lists
"""

import time
import numpy as np

l1 = range(10000)
l2 = range(10000)
st = time.time()
result = [x + y for x, y in zip(l1, l2)]
print(f'The time for the list operations  is {(time.time() - st) * 10000}')

a1 = np.arange(10000)
a2 = np.arange(10000)
st2 = time.time()
result = a1 + a2
print(f'The time for the ND-Array operations  is {(time.time() - st2) * 10000}')
