# Create and Display a Tuple
colors = ("red", "green", "blue")
print(colors)


# Access Tuple Elements
colors = ("red", "green", "blue")

print("First color:", colors[0])
print("Last color:", colors[-1])


# Loop Through Tuple
colors = ("red", "green", "blue")

for color in colors:
    print(color)


# Tuple Length
colors = ("red", "green", "blue")

print("Length of tuple:", len(colors))


# Count and Index
numbers = (10, 20, 30, 20, 40)

print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))


# Convert Tuple to List
colors = ("red", "green", "blue")

colors_list = list(colors)
colors_list.append("yellow")

print(colors_list)


# Tuple Unpacking
student = ("Shreyash", 21, "AI")

name, age, course = student

print(name)
print(age)
print(course)


# Nested Tuple
data = (("A", 1), ("B", 2), ("C", 3))

for item in data:
    print(item)


# Nested Tuple
data = (("A", 1), ("B", 2), ("C", 3))

for item in data:
    print(item)
