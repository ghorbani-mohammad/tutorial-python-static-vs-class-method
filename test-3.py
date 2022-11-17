class Integer(object):
    some_class_attributes = "So true!"

    def __init__(self, number):
        self.number = number

    @classmethod
    def new_number(cls, number):
        print(cls.some_class_attributes)
        return cls(number)


if __name__ == "__main__":
    number = Integer(5)
    print(number.number)

    # Notice that we can create new objects of the class with the class methods
    new_number = Integer.new_number(8)
    print(new_number.number)
