"""
We showed you recently how to extend Stack possibilities by defining a new class
(i.e., a subclass) which retains all inherited traits and adds some new ones.

Your task is to extend the Stack class behavior in such a way so that the class
is able to count all the elements that are pushed and popped (we assume that
counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

introduce a property designed to count pop operations and name it in a way
which guarantees it is hidden;
initialize it to zero inside the constructor;
provide a method which returns the value currently assigned to the counter
(name it get_counter()).
Complete the code in the editor. Run it to check whether your code outputs 100.
"""


class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        """
        Initializes a CountingStack object.

        This class extends the Stack class and adds a counter to keep track of the number of pop operations performed.

        Parameters:
        None

        Returns:
        None
        """
        Stack.__init__(self)
        self.__count_pop = 0

    def get_counter(self):
        """
        Returns the count of pop operations performed on the stack.

        Parameters:
        None

        Returns:
        int: The count of pop operations performed.
        """
        return self.__count_pop

    def pop(self):
        """
        Removes and returns the top element from the stack.

        This method overrides the pop method of the Stack class and increments the counter.

        Parameters:
        None

        Returns:
        Any: The top element of the stack.
        """
        super().pop()
        self.__count_pop += 1


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())  # Returns 100
