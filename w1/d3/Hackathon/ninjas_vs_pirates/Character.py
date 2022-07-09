import random
class Character:
    def __init__(self, name, strength = 10, speed = 10, health = 100):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.health = health
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        return self
    def attack( self , target ):
        if target.speed >= random.randint(0, 20):
            print(f"{target.name} dodged {self.name}'s attack!")
            return self
        else:
            target.health -= self.strength
            return self
    def battle( self, target):
        while self.health or target.health > 0:
            if self.health > 0:
                if target.speed >= random.randint(0, 100):
                    print(f"{target.name} dodged {self.name}'s attack!")
                else:
                    print(f"{self.name} did {self.strength} damage to {target.name}")
                    target.health -= self.strength
                target.show_stats()
            else:
                print(f"{target.name} is the winner!")
                return self
            if target.health > 0:
                if self.speed >= random.randint(0, 100):
                    print(f"{self.name} dodged {target.name}'s attack!")
                else:
                    print(f"{target.name} did {target.strength} damage to {self.name}")
                    self.health -= target.strength
                self.show_stats()
            else:
                print(f"{self.name} is the winner!")
                return self

class Ninja( Character ):

    def __init__(self , name, strength = 10, speed = 60):
        super().__init__(name, strength, speed)
    
    def show_stats( self ):
        super().show_stats()

    def attack( self , target ):
        super().attack(target)

class Pirate( Character ):

    def __init__( self , name, strength = 15, speed = 25, health = 150):
        super().__init__(name, strength, speed, health)

    def show_stats( self ):
        super().show_stats()

    def attack ( self , target ):
        super().attack(target)