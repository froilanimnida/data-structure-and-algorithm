def cubic_example(input_list):
    for i in input_list:  # Outer loop, O(n)
        for j in input_list:  # Middle loop, O(n)
            for k in input_list:  # Inner loop, O(n)
                print(i, j, k)

# this denoted as O(n * n * n) or simply
# O(n^3) cubically