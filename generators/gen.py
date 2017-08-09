from time import time


def add(x, y):
    return x + y


class Adder:

    def __call__(self, x, y):
        return x + y


add2 = Adder()
