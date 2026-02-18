l = [3, 523, 53, 525]

# index = 0
# for item in 1;
#     print(f"The item number at index {index} is {index}")
#     index += 1

# This can be simplify using enumerate function:


for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")