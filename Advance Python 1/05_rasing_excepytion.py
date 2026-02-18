a = int(input("Enter your Number:"))
b = int(input("Enter your Second Nunmer"))

if(b == 0):
    raise ZeroDivisionError("hey your program is not meant to divide nmbers by zero ")
else:
    print(f"The division a/b is {a/b}")