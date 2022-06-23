import random

class Hero:
    def __init__(self, name, superpowers):
        self.name = name
        self.superpowers = superpowers
        self.life_points = random.randint(1, 10)

    def attack(self):
        random_number = random.randint(1, 10)
        return random_number

    def decrease_life(self, decrease_points):
        self.life_points -= decrease_points
        return self.life_points

my_hero = Hero("Sherlock Holmes", "deduction")
# print(my_hero.name, my_hero.superpowers, my_hero.life_points)
# print(my_hero.life_points)
# print(my_hero.attack())
# print(my_hero.decrease_life(3))





