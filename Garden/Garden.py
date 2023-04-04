class Flower:
    def __init__(self, name, water_level=0):
        self.name = name
        self.water_level = water_level


class Tree:
    def __init__(self, name, water_level=0):
        self.name = name
        self.water_level = water_level


class Garden:
    plant = []

    def add_flower(self, flower: Flower):
        self.plant.append(flower)

    def add_tree(self, tree: Tree):
        self.plant.append(tree)

    def show(self):
        for p in self.plant:
            if p.__class__.__name__ == 'Flower':
                if p.water_level < 5:
                    print(f'The {p.name} {p.__class__.__name__}'
                          f' needs water')
                else:
                    print(f'The {p.name} {p.__class__.__name__}'
                          f' doesn\'t need water')
            elif p.__class__.__name__ == 'Tree':
                if p.water_level < 10:
                    print(f'The {p.name} {p.__class__.__name__}'
                          f' needs water')
                else:
                    print(f'The {p.name} {p.__class__.__name__}'
                          f' doesn\'t need water')

    def give_water(self, x):
        number_of_plants = len(self.plant)
        for p in self.plant:
            if p.water_level < 5 and p.__class__.__name__ == 'Flower':
                p.water_level += x / number_of_plants
            elif p.water_level < 10 and p.__class__.__name__ == 'Tree':
                p.water_level += x / number_of_plants


a = Garden()
a.add_flower(Flower('yellow'))
a.add_flower(Flower('blue'))
a.add_tree(Tree('purple'))
a.add_tree(Tree('orange'))
a.show()
a.give_water(40)
a.show()
a.give_water(70)
a.show()
