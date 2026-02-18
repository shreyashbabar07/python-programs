# Write a program to find the gretest of fpour numbers entered by the user.

a1 = int(input("Enter nummber 1: "))
a2 = int(input("Enter nummber 2: "))
a3 = int(input("Enter nummber 3: "))
a4 = int(input("Enter nummber 4: "))


if(a1>a2 and a1>a3 and a1>a4):
    print("Gretest number is a1: ", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Gretest number is a2: ", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Gretest number is a3: ", a3)

elif(a4>a1 and a4>a2 and a4>a4):
    print("Gretest number is a4: ", a4)
