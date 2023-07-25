class Animal:
    def __init__(self, name, terr_req=20):
        self.name = name
        self.terr_req = terr_req


class Zoo:
    animals = []

    def __init__(self, name, territory=100):
        self.name = name
        self.territory = territory

    def place_animal(self, animal: Animal):
        if self.territory > int(animal.terr_req):
            self.animals.append(animal)
            self.territory -= int(animal.terr_req)
            print(f'{animal.name} placed in {self.name}')
        else:
            print('Not enough space')

    def sell(self):
        if len(self.animals) == 0:
            print('No animals to sell')
        else:
            self.animals.sort(key=lambda x: x.terr_req,reverse=True)
            sold = self.animals.pop(0)
            self.territory += int(sold.terr_req)
            return sold

budapest_zoo = Zoo('Budapest Zoo')  # Created with 100 territory
berlin_zoo = Zoo('Berlin Zoo', 200)  # Created with 200 territory
elephant = Animal('elephant', 50)  # Created with 50 territory
giraffe = Animal('giraffe', 40)  # Created with 40 territory
zebra = Animal('zebra')  # Created with 20 territory

budapest_zoo.sell()  # Should print: no animals to sell
budapest_zoo.place_animal(elephant)  # Should print: elephant is placed in Budapest Zoo
budapest_zoo.place_animal(giraffe)  # Should print: giraffe is placed in Budapest Zoo
budapest_zoo.place_animal(zebra)  # Should print: no territory for zebra in Budapest Zoo

berlin_zoo.place_animal(budapest_zoo.sell())  # Should print: elephant is placed in Berlin Zoo
budapest_zoo.place_animal(zebra)  # Should print: zebra is placed in Budapest Zoo
