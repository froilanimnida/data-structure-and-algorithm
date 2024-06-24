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
1. To achieve insertion sort, follow these steps:
2. We have to start with second element of the array as first element in the array is assumed to be sorted.
3. Compare second element with the first element and check if the second element is smaller than swap them.
4. Move to the third element and compare it with the second element, then the first element and swap as necessary to put
    it in the correct position among the first three elements.
5. Continue this process, comparing each element with the ones before it and swapping as needed to place it in the
    correct position among the sorted elements.
6. Repeat until the entire array is sorted.

Time Complexity: O(N^2)
Auxiliary Space: O(1)

Time Complexity of Insertion Sort
Best case: O(n), If the list is already sorted, where n is the number of elements in the list.
Average case: O(n2), If the list is randomly ordered
Worst case: O(n2), If the list is in reverse order

Space Complexity of Insertion Sort
Auxiliary Space: O(1), Insertion sort requires O(1) additional space, making it a space-efficient sorting algorithm.

Advantages of Insertion Sort:
    - Simple and easy to implement.
    - Stable sorting algorithm.
    - Efficient for small lists and nearly sorted lists.
    - Space-efficient.

Disadvantages of Insertion Sort:
    - Inefficient for large lists.
    - Not as efficient as other sorting algorithms (e.g., merge sort, quick sort) for most cases.

Applications of Insertion Sort:
    - Insertion sort is commonly used in situations where:
    - The list is small or nearly sorted.
    - Simplicity and stability are important.

Q1. What are the Boundary Cases of the Insertion Sort algorithm?
    - Insertion sort takes the maximum time to sort if elements are sorted in reverse order. And it takes minimum time
        (Order of n) when elements are already sorted.

Q2. What is the Algorithmic Paradigm of the Insertion Sort algorithm?
    - The Insertion Sort algorithm follows an incremental approach.

Q3. Is Insertion Sort an in-place sorting algorithm?
    - Yes, insertion sort is an in-place sorting algorithm.

Q4. Is Insertion Sort a stable algorithm?
    - Yes, insertion sort is a stable sorting algorithm.

Q5. When is the Insertion Sort algorithm used?
    - Insertion sort is used when number of elements is small. It can also be useful when the input array is almost
    sorted, and only a few elements are misplaced in a complete big array.

Reference from geeks for geeks.
"""

from random import randint
import time
sample_data: list[int] = [23, 1, 10, 5, 2]
new_data: list[int] = [randint(a=0, b=100000) for i in range(10000)]
print(f"Unsorted Array: {new_data}")

start_time = time.time()

for x in range(1, len(new_data)):
    i: int = x
    while i != 0:
        if new_data[i - 1] > new_data[i]:
            new_data[i], new_data[i - 1] = new_data[i - 1], new_data[i]
        i -= 1

end_time = time.time()

elapsed_time_ms = (end_time - start_time) * 1000
print(f"Time it takes to sort the lists in ms: {elapsed_time_ms}")
print(f"Sorted Array: {new_data}")
