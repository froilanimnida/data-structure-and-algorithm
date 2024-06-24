"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the
wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite
high.

In Bubble Sort algorithm,

traverse from left and compare adjacent elements and the higher one is placed at right side.
In this way, the largest element is moved to the rightmost end at first.
This process is then continued to find the second largest and place it and so on until the data is sorted.

Time Complexity: O(N2)
Auxiliary Space: O(1)

Advantages of Bubble Sort:
    - Bubble sort is easy to understand and implement.
    - It does not require any additional memory space.
    - It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in
        the sorted output.

Disadvantages of Bubble Sort:
    - Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
    - Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to
        determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in
        certain cases.

Some FAQs related to Bubble Sort:
What is the Boundary Case for Bubble sort?
    Bubble sort takes minimum time (Order of n) when elements are already sorted. Hence, it is best to check if the
    array is already sorted or not beforehand, to avoid O(N2) time complexity.

Does sorting happen in place in Bubble sort?
    Yes, Bubble sort performs the swapping of adjacent pairs without the use of any major data structure. Hence, Bubble
    sort algorithm is an in-place algorithm.

Is the Bubble sort algorithm stable?
    Yes, the bubble sort algorithm is stable.

Where is the Bubble sort algorithm used?
    Due to its simplicity, bubble sort is often used to introduce the concept of a sorting algorithm. In computer
    graphics, it is popular for its capability to detect a tiny error (like a swap of just two elements) in
    almost-sorted arrays and fix it with just linear complexity (2n).

Example: It is used in a polygon filling algorithm, where bounding lines are sorted by their x coordinate at a specific
scan line (a line parallel to the x-axis), and with incrementing y their order changes (two elements are swapped) only
at intersections of two lines.
"""

from random import randint
import time

list_item = [randint(a=0, b=100000) for i in range(10000)]
print(f"Unsorted list: {list_item}")
start_time = time.time()
while True:
    swapped = False
    for i in range(len(list_item) - 1):
        if list_item[i] > list_item[i + 1]:
            swapped = True
            list_item[i], list_item[i + 1] = list_item[i + 1], list_item[i]
    if not swapped:
        break

end_time = time.time()
elapsed_time_ms = (end_time - start_time) * 1000
print(f"Time it takes to sort the lists in ms: {elapsed_time_ms}")
print(f"Sorted list: {list_item}")
