try:
    a = int(input("Enter your Number "))
    print("")

except Exception as e:
    print(e)

finally:
    print("I am inside the finally")