''' Class Method : A class method is a method which is bound to the class and not the object of the class.@classmethod decoretor is used to creat class method.'''

'''# Syntax :
    @classmethod
        def(cls,p1,p2)'''

class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
    
e = Employee()
e.a = 45

e.show()