'''Inheritance : Inheritance is a way of cerating class from an existing class'''

# Syntax :
'''
class Employee: # Base Class
    # Code

class Programmer(Employee): # Derived or child class
    # code
'''

''' We can use the method and attribute  of "Employee" in "Programmer" object.
    Also we can overwrite and add new attributes and method in "Programer" class '''

'''TYPES OF INHERITANCE
   1. Single Inheritance 
   2. Multiple Inheritance
   3. Multilevel Inheritance'''

#  1. Single Inheritance :  Single Inheritance occurs when child class inherits only a single parent class.

# Example :

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} amd the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")
         
a = Employee()
b = Programmer()
    