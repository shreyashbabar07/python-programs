class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c =3

o = Employee()
print(o.a) # Print the A attribute
#print(a.b) # Show an error as ther is no b attribute in employee class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b)