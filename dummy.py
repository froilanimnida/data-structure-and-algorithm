class Snake:
    def __init__(self, victims):
        self.victims = victims

    def increment(self):
        self.victims += 1


x = Snake(victims=5)
print(x.victims)
x.increment()
print(x.victims)
