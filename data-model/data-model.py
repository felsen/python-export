"""
Some behaviour that i want to implement ->
write some __ function __ is called double _ method or dunder method.

top-level-function / top-level-syntax -> corresponding __ function __.

x + y   -> __add__

init x  -> __init__

repr(x) -> __repr__

x()     -> __call__
"""


class Polynomial:

    def __init__(self, *coffes):
        """
        Initializing the python objects variables.
        """
        self.coffes = coffes

    def __repr__(self, ):
        """
        Printable representation of python objects.
        """
        return "Polynomial(*{!r})".format(self.coffes)

    def __add__(self, other):
        """
        Adding the two polynomial.
        """
        return Polynomial(*(x+y for x, y in zip(self.coffes, other.coffes)))

    def __len__(self, ):
        """
        Defining the length of the polynomial.
        """
        return len(self.coffes)

    def __call__(self, ):
        pass


p1 = Polynomial(1, 2, 3)  # x2 + 2x + 3
p2 = Polynomial(3, 4, 3)  # 3x2 + 4x + 3

