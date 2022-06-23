# Atrybuty:
# # # # name – ‘superman’
# # # # superpowers – lista supermocy np [‘ab’, ‘bc’, ‘cd’]
# # # # life_points – randomowa liczba z zakresu 1-10 - biblioteka random (random.randint)
# # # #
# https://docs.python.org/3/library/random.html#random.randint
# random.choice : https://docs.python.org/3/library/random.html#random.choice
# # #
# # # # Metody:
# # # # attack – return randomowa liczba z zakresu 1-10
# # # # decrease_life  - obniża liczbe punktów życia o podaną ilość
# # # # (x wchodzi jako parameter do funkcji: def decrease_life(self, x) )
# # #
# # # # Tworze obiekt poprzez: superman = Superman()
# import superman from zadanie_superheroes
#

import random


# prob = random.random()


class Superman:
    def __init__(self, name, superpowers=[]):
        self.name = name
        self.superpowers = ['ab','bc','cd']
        self.lifepoints = random.randint(1,10)

    def attack(self):
        atttack = random.randit(1,10)
        return atttack


    def decrease_life(self, x):
        old = self.lifepoints
        self.lifepoints -= x
        print(f'\nTwoje zycie wynosilo {old}, ale zostalo obnizone o {x} i wnynosi teraz {self.lifepoints}')


superman = Superman('superman')
superman.decrease_life(3)

