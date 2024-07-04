"""
3.2.10   LAB   Queue aka FIFO: part 2
Your task is to slightly extend the Queue class's capabilities. We want it to have
a parameterless method that returns True if the queue is empty and False otherwise.

Complete the code we've provided in the editor. Run it to check whether it outputs
a similar result to ours.

Below you can copy the code we used in the previous lab:

Expected output:
1
dog
False
Queue empty

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
            return False
        return self.__queue_items[self.__current_queue - 1]

    def get_length(self):
        return len(self.__queue_items)


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        super().__init__()
        self.__tracker = 0

    def is_empty(self):
        self.__tracker += 1
        if Queue.get_length(self) == 0 or self.__tracker > Queue.get_length(self):
            return True


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.is_empty():
        print(que.get())
    else:
        print("Queue empty")

# Output:
# 1
# dog
# False
# Queue empty
