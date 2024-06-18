list_item = [200, 188, 290, 490, 60, 210, 43, 55, 1001, 5490, 50, 20, 594, 80, 88, 790, 500, 699, 799, 5454, 3432]

while True:
    swapped = False
    for i in range(len(list_item) - 1):
        if list_item[i] > list_item[i + 1]:
            swapped = True
            list_item[i], list_item[i + 1] = list_item[i + 1], list_item[i]
    if not swapped:
        break

print(list_item)
