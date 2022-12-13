"""
Questions
"""

import numpy as np

a = np.arange(1, 31)
m = a.reshape((6, 5))
print(m)
'''
m is:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]
 [26 27 28 29 30]]
'''

'''
Q1: get the sub matrix of"
11, 12
16, 17
'''
print(m[2:4, 0:2])


'''
Q2: index the following cells: 2, 8, 14, 20
'''
print(m[[0, 1, 2, 3], [1, 2, 3, 4]])


'''
Q3: index the following cells: 
4, 5

24, 25
29, 30
'''
print(m[[0, 4, 5], 3:])
