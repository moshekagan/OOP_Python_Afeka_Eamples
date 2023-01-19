import numpy as np

np.random.seed(21)  # This guarantees the code will generate the same set of random numbers whenever executed
random_integers = np.random.randint(1, high=5000, size=(20, 5))
print(random_integers)

# What is the average value of the second column (to two decimal places)
print(random_integers[:, 1])
print(random_integers[:, 1].mean())

# What is the average value of the first 5 rows of the third and fourth columns?
print(random_integers[0:5, 2:4])
print(random_integers[0:5, 2:4].mean())

"""
Find the positions of:

elements in x where its value is *more* than its corresponding element in y, and
elements in x where its value is *equals* to its corresponding element in y.
"""
x = np.array([21, 64, 86, 22, 74, 55, 81, 79, 90, 89])
y = np.array([21, 7,   3, 45, 10, 29, 55,  4, 37, 18])

z = np.array(x[x > y])
print(z)

z = np.array(x[x == y])
print(z)

# Get all items between 5 and 10 from a.

a = np.array([2, 6, 1, 9, 10, 3, 27])
print(a[(a > 5) & (a < 10)])

# How to swap two rows in a 2d numpy array?
arr = np.arange(9).reshape(3, 3)
print(arr)
arr1 = arr[[1, 0, 2], :]
print(arr1)

# Filter the rows of iris_2d
# that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0

iris_2d = np.genfromtxt("iris.csv", delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
print(iris_2d)

print(iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5)])

# How to find the count of unique values in a numpy array?

# Create a new column for volume in iris_2d,
# where volume is (pi x petallength x sepal_length^2)/3

a = np.array([np.around((np.pi * iris_2d[:, 2] * iris_2d[:, 0] ** 2) / 3, 2)])

print(a)
print(a.shape[0], a.shape[1])
print(iris_2d.shape[0])
a = a.reshape(iris_2d.shape[0], 1)
print(a)
print(iris_2d)
iris_2d = np.hstack((iris_2d, a))
print(iris_2d)

# Find the most frequent value of petal length (3rd column) in iris dataset.
l = np.unique(iris_2d[:, 2])
print(l)
cnt = np.array([])
for x in l:
    c = iris_2d[(iris_2d[:, 2] == x)].shape[0]
    print(c)
    cnt = np.append(cnt, c)
print(cnt)
l = np.vstack([l, cnt])
print(l)
print(l[1, :].max())
mx = l[1, :].max()
print(l[0, l[1, :] == mx])
