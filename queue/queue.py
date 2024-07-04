"""
3.2.9   LAB   Queue aka FIFO
As you already know, a stack is a data structure realizing the LIFO (Last In –
First Out) model. It's easy and you've already grown perfectly accustomed to it.

Let's try something new now. A queue is a data model characterized by the term
FIFO: First In – First Out. Note: a regular queue (line) you know from shops or post offices
works exactly in the same way – a customer who came first is served first too.

Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the
result (the queue cannot be empty to successfully perform it.)
Follow the hints:

use a list as your storage (just like we did with the stack)
put() should append elements to the beginning of the list, while get() should
remove the elements from the end of the list;
define a new exception named QueueError (choose an exception to derive it from)
and raise it when get() tries to operate on an empty list.
Complete the code we've provided in the editor. Run it to check whether its
output is similar to ours.

Expected output:
1
dog
False
Queue error
"""


class QueueError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Queue:
    def __init__(self):
        self.__queue_items = []
        self.__queue_length = 0
        self.__current_queue = 0

    def put(self, elem):
        self.__queue_items.append(elem)
        self.__queue_length += 1

    def get(self):
        if len(self.__queue_items) == 0:
            raise QueueError
        self.__current_queue += 1
        if self.__current_queue > self.__queue_length:
            raise QueueError
        return self.__queue_items[self.__current_queue - 1]


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error")

# Output:
# 1
# dog
# False
# Queue error
