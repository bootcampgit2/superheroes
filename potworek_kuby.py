import random


class Potworek:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1,10)

    def attack(self):
        return random.randint(1,10)

    def decrease_life(self, x):
        self.life_points -= x


super_potworek = Potworek ('Potwor', ['gryzak','krzyk'])

print(super_potworek.attack())
print(super_potworek.life_points)
super_potworek.decrease_life(1)
print(super_potworek.life_points)
