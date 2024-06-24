"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest)
element from the unsorted portion of the list and moving it to the sorted portion of the list.

The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it
with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the
entire list is sorted.

Complexity Analysis of Selection Sort
Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:
    - One loop to select an element of Array one by one = O(N)
    - Another loop to compare that element with every other Array element = O(N)
    - Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)

Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The
selection sort never makes more than O(N) swaps and can be useful when memory writing is costly.

Advantages of Selection Sort Algorithm
    - Simple and easy to understand.
    - Works well with small datasets.

Disadvantages of the Selection Sort Algorithm
    - Selection sort has a time complexity of O(n^2) in the worst and average case.
    - Does not work well on large datasets.
    - Does not preserve the relative order of items with equal keys which means it is not stable.

How it works:

1. Go through the array to find the lowest value.
2. Move the lowest value to the front of the unsorted part of the array.
3. Go through the array again as many times as there are values in the array.
"""

from random import randint
import time

sample_data: list[int] = [64, 25, 11]
new_data: list[int] = [randint(a=0, b=100000) for x in range(10000)]
print(f"Unsorted data: {new_data}")

start_time = time.time()

for x in range(len(new_data) - 1):
    lowest_elem_index = x
    for y in range(x, len(new_data)):
        if new_data[lowest_elem_index] > new_data[y]:
            lowest_elem_index = y
    else:
        new_data[x], new_data[lowest_elem_index] = new_data[lowest_elem_index],  new_data[x]

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Time it takes to sort the lists in ms: {elapsed_time_ms}")
print(f"Sorted data: {new_data}")
