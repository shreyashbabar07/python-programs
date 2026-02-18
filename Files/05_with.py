f = open("file.txt")
print(f.read())
f.close()

# Tise same can be written using with statment like this:

with open("file.txt") as f:
    print(f.read())

# You dont have to exactely close the file