my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print("Original List: ")
print(my_list)
print("The list with unique elements only:")
print(new_list)
