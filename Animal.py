# Create an Animal class
#
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# When creating a new animal instance these values must be set to the default 50 value
# Every animal can eat() which decreases its hunger by one
# Every animal can drink() which decreases its thirst by one
# Every animal can play() which increases both its hunger and thirst by one

class Animal:
    def __init__(self, hunger=50, thirst=50):
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1
        return self.hunger

    def drink(self):
        self.thirst -= 1
        return self.thirst

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger, self.thirst


horse = Animal(hunger=60, thirst=70)
print(horse.eat())
print(horse.drink())
print(horse.play())
