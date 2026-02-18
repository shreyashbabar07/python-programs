marks = {
    "Shreyash" : 100,
    "Samarth" : 95,
    "Vinayak" : 56
}

print(marks.items())

print(marks.keys())
print(marks.values())

marks.update({"Shreyash" : 99})
print(marks)

# print(marks.get("Shreyash2"))  #prints none
# print(marks["Shreyash2"])     # print return error

print(marks.clear())
