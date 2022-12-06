# a is b is equivalent to id(a) == id(b)

# Value can be defined as what the == operator compares,
# so any time a == b, you can say that a and b have the same value
# If a class doesn't define an __eq__ method (to implement the == operator),
# it will inherit the default version from object
# and its instances will be compared solely by their identities

# In addition to a value, some objects have a hash value,
# which means they can be used as dictionary keys (and stored in sets).
# The function hash(a) returns the object a's hash value,
# a number based on the object's value.
# The hash of an object must remain the same for the lifetime of the object,
# so it only makes sense for an object to be hashable if its value is immutable
# (either because it's based on the object's identity,
# or because it's based on contents of the object that are themselves immutable).
"""

hash(obj, /)
    Return the hash value for the given object.

    Two objects that compare equal must also have the same hash value, but the
    reverse is not necessarily true.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name}'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(tuple([self.name, self.age]))


p1 = Person('John', 22)
p2 = Person('Jane', 22)
p3 = p1
print(hash(p1))
print(p1)
t = (p1, p2)
print(t)

d = {}
d[p1] = [70, 90]
d[p2] = [45, 67]
for p in d:
    print(f'{p} : {d[p]}')


print(id(p1))
print(hash(p1))
print(id(p2))
print(hash(p2))
print(id(p3))
print(hash(p3))


# another example

# Incorrect: equality method defined but class contains no hash method
class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False

        return self._x == other._x and self._y == other._y


# Improved: equality and hash method defined (inequality method still missing)
class PointUpdated(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash(self._x) ^ hash(self._y)


# Improved: equality method defined and class instances made unhashable
class UnhashablePoint(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Point({self._x}, {self._y})'

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    # Tell the interpreter that instances of this class cannot be hashed
    __hash__ = None
