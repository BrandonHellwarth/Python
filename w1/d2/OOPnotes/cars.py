#snake_case
#camelCase-JS functions
#PascalCase-python classes
class Car:
    def __init__(self, make, model, color = 'blue'):
        #you can add default values to the parameters
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False
    def turn_on(self):
        self.is_running = True
    def drive(self):
        if self.is_running:
            print("driving")
        else:
            print("cannot drive because I am not started")

car_a = Car('toyota', 'rav4', 'blue')
car_b = Car('tesla', 'model S', 'yellow')

car_a.turn_on()

car_a.drive()
car_b.drive()

print(car_a.make)
print(car_b.color)