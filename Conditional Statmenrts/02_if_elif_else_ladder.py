a = int(input("Enter your age: "))

# If elif else ladder

if(a>18):
    print("You are above age consent")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering a 0 which is not valid in age")

else:
    print("You are blelow the age of consent")