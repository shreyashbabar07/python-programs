# Create and Display a List
fruits = ["apple", "banana", "mango", "orange"]
print("Fruits List:", fruits)

# Access List Elements
fruits = ["apple", "banana", "mango", "orange"]

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add Elements
fruits = ["apple", "banana"]

fruits.append("mango")       # add at end
fruits.insert(1, "orange")   # add at index

print(fruits)

# Remove Elements
fruits = ["apple", "banana", "mango", "orange"]

fruits.remove("banana")   # remove by value
fruits.pop()              # remove last element

print(fruits)

# Sort and Reverse
numbers = [5, 2, 9, 1, 7]

numbers.sort()
print("Sorted:", numbers)

numbers.reverse()
print("Reversed:", numbers)

# Find Length and Count
fruits = ["apple", "banana", "apple", "mango"]

print("Length:", len(fruits))
print("Apple count:", fruits.count("apple"))

# Loop Through List
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# List Comprehension
numbers = [1, 2, 3, 4, 5]

squares = [x*x for x in numbers]
print(squares)
