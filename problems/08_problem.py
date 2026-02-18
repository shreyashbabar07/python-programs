# Write a python program to find max in Array

arr = [10, 20, 30, 54, 87]

max_element = arr[0]

for num in arr:
    if num > max_element:
        max_element = num

print("Maximum element in the Array is:", max_element)


# Exmple 2 :

arr =  [12, 23, 25, 50, 71]

print("maximum number in the Array: ", max(arr))


arr = [10, 23, 25, 56, 89]

print("minimum number in the Array is: ", min(arr))