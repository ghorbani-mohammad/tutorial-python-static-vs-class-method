class Item(object):
    rock = False
    paper = True
    scissor = False

    def __init__(self, number):
        self.number = number

    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def class_method(cls):
        print(
            f"This is a class method that belongs to {cls} and the paper is {cls.paper}"
        )
