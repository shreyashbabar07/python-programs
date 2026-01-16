# Find largest number of three number

a = int(input("Enter a First number:"))
b = int(input("Enter a Second number:"))
c = int(input("Enter a Third number:"))

if a > b and a > c:
    print("a is the largest")
elif b > c:
    print("b is the largest")
else:
    print("c is the largest")