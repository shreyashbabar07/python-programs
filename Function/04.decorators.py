'''Decorators: 
    Decorstors add extra behaviour to a function, without changing the functions code
    A Decoratos is a function that take another function as input and return a new function'''

# Basic Decorator : Define the decorator first, then apply it with @decorator_name above the function.

# A basic decorator that uppercases the return value of the decorated function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello"

print(myfunction())

# Multiple Decoretors: A decorator can be called multiple times. Just place the decorator above the function you want to decorate.

# Example: Using the @changecase decorator on two functions:

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunction())
print(otherfunction())

'''Arguments in the Decorated Function: Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:'''

# Example : Functions with arguments can also be decorated:

def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

'''Decorator With A : Decorators can accept their own arguments by adding another wrapper level.'''

# Example: A decorator factory that takes an argument and transforms the casing based on the argument value.

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

'''Multiple Decorators :
    You can use multiple decorators on one function.

    This is done by placing the decorator calls on top of each other.

    Decorators are called in the reverse order, starting with the one closest to the function.'''

# Example : One decorator for upper case, and one for adding a greeting:

def changecase(func):
   def myinner():
      return func().upper()
   return myinner

def addreeting(func):
   def myinner():
      return "Hello" + func() + " Have a good day!"
   return myinner

@changecase
@addreeting
def myfunction():
   return "Shreyash"

print(myfunction())