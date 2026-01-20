'''Arguments:
    Information can be passed into functions as arguments.

    Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

    The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:'''

# A Function with one argument
def my_function(fname):
    print(fname + "Refsnes")

my_function("Samarth")
my_function("Shreyash")
my_function("Vinayak")


'''From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called.'''

def my_function(name):  # name is parameter
    print("Hello", name)

my_function('Shreysh') # Shreyash is an argument


'''Default Parameter Values:
You can assign default values to parameters. If the function is called without an argument, it uses the default value:'''

def my_function(name = "friend"):
    print("Hello", name)

my_function("Shreyash")
my_function("Samarth")
my_function()
my_function("Vinayak")

# Default value for Countray Parameter
def my_function(country = "India"):
    print(" I am frome", country)

my_function("India")
my_function("Russia")
my_function()
my_function("Japan")

''' Positional Arguments :
    When you call a function with arguments without using keywords, they are called positional arguments.

    Positional arguments must be in the correct order: '''

# Example:
def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "name is", name)

my_function("dog", "buddy")

# Swiching the order 
def my_funnction(animal, name):
    print("I have a", animal)
    print("My", animal + "name is" + name)

my_function("Buddy", "Dog")


'''Positional Arguments :
    When you call a function with arguments without using keywords, they are called positional arguments.

    Positional arguments must be in the correct order:'''

def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

'''Passing Different Data Types :
    You can send any data type as an argument to a function (string, number, list, dictionary, etc.).

    The data type will be preserved inside the function:'''

# Sending a list as an argument:
def my_function(fruits):
    for fruits in fruits:
        print(fruits)

my_fruits = ["apple","banana","cherry"]
my_function(my_fruits)

# Sending a dictionary as an argument:
def my_function(persion):
    print("Name:", persion["name"])
    print("Age:", persion["age"])

my_person = {"name": "Shreyash", "age": 21}
my_function(my_person)

'''Returning Different Data Types :
    Functions can return any data type, including lists, tuples, dictionaries, and more.'''

# A function that returns a list:
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

#A function that returns a tuple:

def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)