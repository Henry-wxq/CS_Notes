"""
*args: collects all inputs into a tuple, which can use index to access

**kwargs: collects all inputs into a dictionary, which can use key to access
look through all the inputs and find the ones that i want and use them to do something
"""

# this function add can take any number of arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

# create unlimited keyword arguments
# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
#
#     print(kwargs["add"])

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]



if __name__ == "__main__":
    add(3, 5, 6, 7, 8, 9, 10)

    # calculate(add=3, multiply=5)
    # {'add': 3, 'multiply': 5}

    calculate(2, add=3, multiply=5)
    # 25

    my_car = Car(make="Ford", model="Mustang")
