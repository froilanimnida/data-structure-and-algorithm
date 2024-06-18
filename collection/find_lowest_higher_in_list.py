my_list = [11, 23, 123, 3434, 54, 2, 4354, 123, 65, 32, 54, 654, 234, 213, 53]
lowest_item = my_list[0]
highest_item = my_list[0]

# Find the lowest number in the list.
for item in my_list:
	if item > lowest_item:
		lowest_item = item

# Find the highest number in the list
for item in my_list:
	if item < highest_item:
		highest_item = item

print(f"The lowest item in the list is {lowest_item}.")
print(f"The highest item in the list is {highest_item}.")
