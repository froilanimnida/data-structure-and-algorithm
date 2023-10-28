def quadratic_example(input_list):
    for i in input_list:  # Outer loop, O(n)
        for j in input_list:  # Inner loop, O(n)
            print(i, j)
# this function has runtime complexity of
# O(n * n) or simply O(n^2)