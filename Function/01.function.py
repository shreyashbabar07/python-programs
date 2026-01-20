''' Python Functions:
    A function is a block of code which only runs when it is called.
    A function can return data as a result.
    A function helps avoiding code repetition.'''

# Creating a Function
def my_function():
    print("Hello world!")

# Calling a Function
def my_function():
    print("Hello World")   

my_function()

# Calling same function multiple times
def my_function():
    print("Hello World")

my_function()
my_function()
my_function()

# EXAMPLE
def fahrenheit_to_celsius(fahrenhet):
    return (fahrenhet - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

''' Return Values:
    Functions can send data back to the code that called them using the return statement.
    When a function reaches a return statement, it stops executing and sends the result back: '''

# A function that return a value
def get_greeeting():
    return "Hello"

message = get_greeeting()
print(message)

# Using a return value derectly
def get_greeeting():
    return "Hello"
print(get_greeeting())


'''The pass Statment : Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement:'''

#Example:

def my_function():
    pass