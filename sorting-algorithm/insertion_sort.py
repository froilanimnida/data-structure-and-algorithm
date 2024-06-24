"""
Insertion sort is a simple sorting algorithm that works by iteratively
inserting each element of an unsorted list into its correct position in a
sorted portion of the list. It is a stable sorting algorithm, meaning that
elements with equal values maintain their relative order in the sorted output.

Insertion sort is like sorting playing cards in your hands. You split the cards
into two groups: the sorted cards and the unsorted cards. Then, you pick a card
from the unsorted group and put it in the right place in the sorted group.

Insertion Sort Algorithm:
Insertion sort is a simple sorting algorithm that works by building a sorted
array one element at a time. It is considered an “in-place” sorting algorithm,
meaning it doesn't require any additional memory space beyond the original
array.

Algorithm:

To achieve insertion sort, follow these steps:

We have to start with second element of the array as first element in the
array is assumed to be sorted.

Compare second element with the first element and check if the second element
is smaller than swap them.

Move to the third element and compare it with the second element, then the
first element and swap as necessary to put it in the correct position among
the first three elements.

Continue this process, comparing each element with the ones before it and
swapping as needed to place it in the correct position among the sorted
elements.

Repeat until the entire array is sorted.

Reference from geeks for geeks.
"""

from random import randint
sample_data: list[int] = [23, 1, 10, 5, 2]
new_data: list[int] = [randint(a=0, b=10000) for i in range(25)]
print(f"Unsorted Array: {new_data}")

for x in range(1, len(new_data)):
    i: int = x
    while i != 0:
        if new_data[i - 1] > new_data[i]:
            new_data[i], new_data[i - 1] = new_data[i - 1], new_data[i]
        i -= 1

print(f"Sorted Array: {new_data}")
