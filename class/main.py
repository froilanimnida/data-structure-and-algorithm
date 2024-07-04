from typing import Literal


class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self) -> Literal['Arf Arf Arf']:
        return "Arf Arf Arf"


x = Dog("Leet")

print(x.speak())
