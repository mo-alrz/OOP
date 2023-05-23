class Aircraft:
    def __init__(self, damage=0, ammo=0):
        self.ammo = ammo
        self.damage = damage

    def fight(self):
        total_damage = self.damage * self.ammo
        return total_damage

    def refill_ammo(self, x):
        unused_ammo = x - self.ammo
        self.ammo += self.ammo
        return unused_ammo

    def get_type(self):
        return self.__class__.__name__

    def get_status(self):
        return f'Type: {self.__class__.__name__} Ammo: {self.ammo} Base Damage: {self.damage} All Damage: {self.fight()}'


class F16(Aircraft):
    def __init__(self, damage, ammo):
        super().__init__(damage, ammo)


class F35(Aircraft):
    def __init__(self, damage, ammo):
        super().__init__(damage, ammo)


a = []
first = F16(30, 8)
a.append(first)
second = F35(50, 12)
a.append(second)
for i in a:
    print(i.fight())
    print(i.refill_ammo(200))
    print(i.get_status())
    print(i.get_type())
