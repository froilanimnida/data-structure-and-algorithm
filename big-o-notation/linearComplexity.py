# This shows that runtime complexity grows linearly
# on the input size.

def linear_example(input_list):
    for item in input_list:
        print(item)

def linear_example(input_list, second_input_lists):
    for item in input_list:  # Represents O(n)
        print(item)
    for item in second_input_lists:  # Represents O(m)
        print(item)
    # Runtime complexity is O(n + m)
    # When analyzing the overall time complexity,
    # you simply add the complexities together to get
    # O(n + m), which represents a linear growth in time
    # with respect to the combined sizes of both input lists.
