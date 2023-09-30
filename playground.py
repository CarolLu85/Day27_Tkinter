# Unlimited Positional Arguments
def add(n1, n2):
    return n1 + n2

add(n1 = 1, n2 = 2)
def add(*args):
# args in a form of tuple
    for n in args:
        print(n)
add(3,5,7,8)


def add(*args):
    print(args[1])
    print(type(args))
    for n in args:
        return sum(args)
    # sum = 0
    # for n in args:
    #     sum += n
    # return sum

n = add(3,4,5,6)
print(n)


# **kwargs: Many Keyworded Arguments
def calculate(n, **kwargs):
    # print(kwargs)--dictionary
    # for key, value in kwargs.items():
    #     print(key)
    #     print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # another way of above two lines, when "make" or "model" is not given as an argument
        # it wont crash, get error.
        self.make = kw.get("make")
        self.make = kw.get("colour")
        self.model = kw.get("model")

# my_car = Car(make="Nissan", model="GT-R")  ---- the lines of self.make=kw["make"]
my_car = Car(make="Nissan", model="SkyLine")
print(my_car.make)
print(my_car.model)
