from random import choice

COLORS = ["Brown", "Black", "Golden"]


class Animal(object):
    def __init__(self, color):
        self.color = color

    @classmethod
    def make_baby(cls):
        color = choice(COLORS)
        print(cls)
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
        print("making dog baby")
        # We will do something dog specifics here
        return super(Dog, cls).make_baby()


class Cat(Animal):
    pass


if __name__ == "__main__":
    d = Dog("Brown")
    print(d.color)

    pup = d.make_baby()  # Which class do you think will be printed? Dog or Animal
    print(pup.color)


# So you can see that we also can override static methods in subclassing
