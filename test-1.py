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


if __name__ == "__main__":
    # The note here is that you can run both static method and class
    # method with the class itself and class object
    i = Item(8)
    i.static_method()
    i.class_method()
    Item.static_method()
    Item.class_method()
