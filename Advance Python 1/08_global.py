a = 34

def fun():
    # Global a
    a = 3
    print(a)

fun()
print(a)