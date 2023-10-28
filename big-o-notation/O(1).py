# O(1). This function runs at constant time (doesn't change)
def printing(numbers):
  print(numbers[0]) # this takes constant amount of time
  print(numbers[0]) # this takes constant amount of time

# this can be O(2) or simply O(1)
# because we're running the same operation even if we have
# one million inputs our method runs at constant time.
