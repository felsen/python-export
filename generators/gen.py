from time import time
from time import sleep


def add(x, y):
    return x + y


class Adder:

    def __call__(self, x, y):
        return x + y


add2 = Adder()


def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)
    return rv


class Compute:

    def __call__(self, ):
        rv = []
        for i in range(10):
            sleep(5)
            rv.append(i)
        return rv


com = Compute()
