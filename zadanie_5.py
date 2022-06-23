import random

class Heroe:
    def __init__(self, name, superpowers, life_points):
        self.name = name
        self.superpowers = superpowers
        self.life_points = life_points

    def attack(self):
        self.life_points = random.randint(1, 10)
        return self.life_points

    def decrease_life(self, decrease_points):
        self.life_points -= decrease_points
        return self.life_points

my_hero = Heroe("Sherlock", 'deduction', 100)
print(my_hero.name, my_hero.superpowers, my_hero.life_points)
print(my_hero.attack())
print(my_hero.decrease_life(3))





