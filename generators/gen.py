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

    def __iter__(self, ):
        self.last = 0
        return self

    def __next__(self, ):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv


com = Compute()
for val in com:
    print(val)
