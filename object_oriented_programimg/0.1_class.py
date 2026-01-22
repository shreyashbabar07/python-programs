'''Class : classs is a Bluprint of creating object'''

#Syntax :
class Employee:    # Class name is writeen in pascal case
    print()  # Methods & variables 

class Employee:
     name = "Shreyash"
     language = "Py"
     salary = 1200000

Shreyash = Employee() # Object
print(Shreyash.name, Shreyash.language)

''' Object : Object is an instantation (Instance) of class. When class is defined a tenolet (into) is defined. Memorry is allocated only after instantation
             Object of a given calss can invoke the methods available to it without reveling the implementation detailed to user - Abstaction & encapsulation!'''

''' Modeling A Problen In OOPS : 
    We identify following in our problem
    1. Noun - Class- Employee
    2. Adjective - Attributes-name,age,salary
    3. Verbs - Methods -getSalary(),inrement()'''

class Employee:
     name = "Shreyash"
     language = "Py"
     salary = 1200000

Shreyash = Employee() # Object
print(Shreyash.language, Shreyash.language)

'''CLASS ATTRUBUTES : An attribute the belongs to the calss rether than a particular object.'''

class Employee:
     company = "Gogle" # Specific to each class
shreyash = Employee() # Object Instatition
shreyash.company
Employee.company = "Youtube" # Chenging Class attribute

#Example :

class Employee:
     name = "Shreyash"
     language = "Py"   # This is an class attribute
     salary = 1200000

shreyash = Employee() 
shreyash.name = "Shryeash"  # This is an object attribute
print(Shreyash.name, Shreyash.language, Shreyash.language)

Rohan = Employee() 
Rohan.name = "Rohan"
print(Rohan.name, Rohan.language, Rohan.language)

# here is an v instance attribute abd ssalary and language are class attributes as they directly belong to the class

'''INSTANCE ATTRIBUTES : An attribute that belongs to the instance (object). Assuming the class from the previous example:'''

class Employee:
     language = "Python" # This is a class attribute
     salary = 120000

shreyash = Employee()
shreyash.language = "javascript" # This is an instance attribute

'''SELF PARAMETER : self refers to the instance of the class. it is automatically passed with a function call from ac object.'''

#Syntax: 
# shreyash.grtSalary() # here self is shreyash
# equivanant to Employee.getSalary(herry)

# The Function get.Salary() id defined as:

class Employee:
     company = "Google"
     def getSalary(self):
          print("Salary is not there")



