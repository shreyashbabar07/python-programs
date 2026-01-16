# Creating a list with duplicat value
data = [1, 2, 3, 1,  4 , 2, 5]

# Converting list to set remove duplicates
unique_set = set(data)

# Converting set back to list
unique_list = list(unique_set)

# Printing orignal and updated list 
print("Orignal List:", data)
print("List without duplicates:", unique_list)