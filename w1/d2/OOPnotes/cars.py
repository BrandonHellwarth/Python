#snake_case
#camelCase-JS functions
#PascalCase-python classes
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
    def turn_on(self):
        self.is_running = True
    def drive(self):
        if self.is_running:
            print("driving")
        else:
            print("cannot drive because I am not started")

car_a = Car('toyota')
car_b = Car('tesla', 'model S', 'yellow')

car_a.turn_on()

car_a.drive()
car_b.drive()

print(car_a.make)
print(car_b.color)