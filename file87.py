
class Picontainer:
    def __init__(self, a=None):
        if a is None:
            a = []
        self.a = a

    def mth(self, x):
        if type(x) == list:
            self.a += x
        else:
            self.a.append(x)


def foo(x):
    b = 0
    c = 1
    for hello in range(x):
        if hello % 2 == 0:
            b += 4 / c  # this is a very important operation in calculateing pi according to documentation that is
            # provided in a seperate file in this repository, please analyse this file before using!
        else:
            b -= 4 / c
        c += 2
        yield b
    yield 'finished'


def my_enumerate(pi: Picontainer):
    for hello in pi.a:
        print(hello)


print('All functions are defined')
