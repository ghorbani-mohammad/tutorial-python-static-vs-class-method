from random import choice

COLORS = ["Brown", "Black", "Golden"]


class Animal(object):
    def __init__(self, color):
        self.color = color

    @classmethod
    def make_baby(cls):
        color = choice(COLORS)
        return cls(color)

    @staticmethod
    def speak():
        print("Roar")


class Dog(Animal):
    @staticmethod
    def speak():
        print("Bark")

    @classmethod
    def make_baby(cls):

        return super().make_baby()


class Cat(Animal):
    pass
