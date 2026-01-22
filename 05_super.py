'''SUPER METHOD : super() method is used to method of a super class in the derived class'''

# Syntax :
# super().__init__()  # __init__() Calls constructor of the base class.

# Example :

class Employee: 
        def __init__(self):
            print("Constuctor of Employee")
        a = 1

class Programmer(Employee):
        def __init__(self):
            print("Constructor of Programmer")
        b = 2

class Manager(Programmer):
        def __init__(self):
            super().__init__()   # Super()
            print("Constructor of Manager")
        c = 3

# o = Employee()
# print(o.a) # print the attribute

#o = Programmer()
#print(o.a, o.b) 

o = Manager()
git print(o.a, o.b, o.c)