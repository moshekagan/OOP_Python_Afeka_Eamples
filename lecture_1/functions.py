# Example 1 - define function
def my_function1():
  print("Hello from a function")

# Example 2 - call to function function
my_function1()  #"Hello from a function"


# Example 3 - parameters
def my_function2(name):
  print(f"Hi {name}!")

my_function2("Dan")
my_function2("Ron")
my_function2("Lior")
# Hi Dan!
# Hi Ron!
# Hi Lior!


# Example 4 - number of parameters
def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Donald", "Duck")
# Donald Duck


# Example 5 - Default parameter value
def my_function4(country="Israel"):
  print("I am from " + country)

my_function4("Sweden")
my_function4("India")
my_function4()
my_function4("Brazil")
# I am from Sweden
# I am from India
# I am from Israel
# I am from Brazil


# Example 6 - list as parameter
def my_function6(fruits):
  for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function6(fruits)
# apple
# banana
# cherry


# Example 7 - return value
def my_function7(x):
  return 5 * x

print(my_function7(3))
print(my_function7(5))
print(my_function7(9))
# 15
# 25
# 45

# Example 7 - pass
def myfunction():
  pass