my_list = [11, 23, 123, 3434, 54, 2, 4354, 123, 65, 32, 54, 654, 234, 213, 53]
target = 213
found = False
# for multiple occurrence
for i in range(len(my_list)):
  if my_list[i] == target:
    found = True
    print(f"The item {target} found at index {i}")

if not found:
  print(f"The item {target} wasn't found on the list")

# for single or the first instance
for i in range(len(my_list)):
  if my_list[i] == target:
    print(f"The item {target} found at index {i}")
    break
else:
  print(f"The item {target} wasn't found on the list")
