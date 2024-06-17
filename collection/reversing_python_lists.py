my_list = [10, 20, 30, 40, 50, 60, 70, 80]
for item in range(len(my_list) // 2):
    my_list[item], my_list[len(my_list) - 1 - item] = my_list[len(my_list) - 1 - item], my_list[item]
print(my_list)
