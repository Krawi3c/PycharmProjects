def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(5, 7, 9, 15, 3, 1))


def calculate(n, **kwargs):

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(n=2, add=3,multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Audi")
print(my_car.model)

# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
# my_car = Car(make="Audi")
# print(my_car.model)
