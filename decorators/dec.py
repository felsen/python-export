from time import time


def timer(func):
    def wraps(*a, **kw):
        before = time()
        rv = func(*a, **kw)
        after = time()
        print("Time taken", after - before)
        return rv
    return wraps


def mtimes(n):
    def ntimer(func):
        def wrapper(*a, **kw):
            for _ in range(n):
                print("sub")
                rv = func(*a, **kw)
            return rv
        return wrapper
    return ntimer


@mtimes(4)
def add(x, y=10):
    return x + y


print("add(10)", add(10))
print("add(20, 30)", add(20, 30))
print("add(40, 50)", add(40, 50))
