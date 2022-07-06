#snake_case
#camelCase-JS functions
#PascalCase-python classes
from operator import truediv


class Car:
    def __init__(self, make, model = 'rav4', color = 'blue'):
        #you can add default values to the parameters
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    def info(self):
        print("*"*80)
        print(f"make: {self.make}")
        print(f"model: {self.model}")
        print(f"color: {self.color}")
        return self
    def turn_on(self):
        self.is_running = True
        return self
    def drive(self):
        if self.is_running:
            print("driving")
        else:
            print("cannot drive because I am not started")
        return self
    @classmethod#targets all items in class
    def change_creator(cls, new_creator):
        cls.creator = new_creator
    @staticmethod#targets no items in class
    def is_appropriate_color(color):
        color_list = ['blue', 'black', 'white']
        if color in color_list:
            return True
        else:
            return False
car_a = Car('toyota')
car_b = Car('tesla', 'model S', 'yellow')

car_a.turn_on()
car_b.is_running = True

car_a.drive()
car_b.drive()

print(Car.is_appropriate_color(car_b.color))

Car.change_creator("Brandon")

print(car_a.make)
print(car_b.color)