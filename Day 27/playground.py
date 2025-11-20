from numpy.ma.core import multiply


# def add(*numbers):
#     print((numbers[2]))
#
#
#     total=0
#     for num in numbers:
#         total +=num
#     return total


# print(add(5,10,15,20,25))

# def calculate(n,**kwargs):
#     print(kwargs)
#
#     n*=kwargs["multiply"]
#     n+=kwargs["add"]
#     print(n)
#
#
# calculate(5, add=5, multiply=10)


class Car:
    def __init__(self, **kw):
        self.make=kw.get("make")
        self.model=kw.get("model")
        self.color=kw.get("color")
        self.seats=kw.get("seats")

my_car =  Car(make="Nissan", model="Skyline",color="Red", seats="Pure Leather")
print(my_car)

