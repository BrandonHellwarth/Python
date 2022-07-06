#person class
#shoe class
#any modificattion on an instance within a class should be done with a method or function within the class. No external functions!
class Person:
    def __init__(self, first_name, last_name, height, weight, age, shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.age = age
        self.shoe_size = shoe_size
        self.shoes = []
        self.miles = 0
        self.fullname = f"{first_name} {last_name}"

        def info(self):
            print("*"*80)
            print(f"fullname: {self.fullname}")
            print(f"height: {self.height}")
            print(f"weight: {self.weight}")
            print(f"age: {self.age}")
            print(f"shoe_size: {self.shoe_size}")
            print(f"miles: {self.miles}")
            self.shoes_info()
            print("shoes:")
            print("*"*80)
            return self

        def shoes_info(self):
            for index, shoe in enumerate(self.shoes):
                print("^"*80)
                print(f"Shoe number: {index + 1}")
                shoe.info()
                print("^"*80)
            return self

        def walk(self):
            distance = input("How far do you want to walk?")
            print("Your Shoes...")
            self.shoes_info()
            shoe_chosen = input("What shoes do you want to walk in?")
            shoe_index = int(shoe_chosen) - 1
            shoe_actual = self.shoes[shoe_index]
            shoe_actual.add_miles(distance)
            self.miles += distance

        def get_shoes(self, shoe):
            if shoe.size != self.shoe_size:
                print("you can't have that shoe")
                return self
            self.shoes.append(shoe)
            print("You have recieved a new pair of shoes")
            return self

class Shoe:
    def __init__(self, brand, color, style, size):
        self.brand = brand
        self.color = color
        self.style = style
        self.size = size
        self.miles = 0

    def info(self):
        print(f"brand: {self.brand}")
        print(f"color: {self.color}")
        print(f"style: {self.style}")
        print(f"size: {self.size}")
        print(f"miles: {self.miles}")
        return self

    def add_miles(self, amount):
        self.miles += amount
        return self

p1 = Person('Sarah', 'somner', 142, 50, 20, 8.5)
s1 = Shoe('Nike', 'Green', 'low', 10)
s2 = Shoe('nike', 'green', 'low', 8.5)
s3 = Shoe('nike', 'brown', 'low', 8.5)

is_playing = True #random boolean variable not linked to anything

p1.get_shoes(s2).get_shoes(s3)
while is_playing:
    if p1.miles >= 150:
        is_playing = False
        break
    p1.walk()
    p1.info()