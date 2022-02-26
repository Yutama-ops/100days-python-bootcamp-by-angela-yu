def cal(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(cal(5, 5, 5, 5, 2, 3, 10))

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    # if kwargs["add"]:
    #     print(kwargs["add"] + n)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, multiply = 5, add = 9)

class Car:

    def __init__(self, **kwargs):
        # .get return none
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")

my_car = Car(make = "Mercedes", model = "I8")

print(my_car.make)
print(my_car.color)