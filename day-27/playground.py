def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(n=2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make") # no error
        self.model = kw.get("model")

my_car = Car(make = "Nissan", model="GT-R")
print(my_car.model)