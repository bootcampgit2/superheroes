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



class Superbohater:
    def __init__(self,name):
        self.name = name
        self.superpowers = ['ab','cd','ef']
        self.life_points = random.randint(1,10)

    def attack(self):
        print(random.randint(1,10))
    def decrease_life(self,x):
        print(self.life_points - x)

superman = Superbohater('superman')
print(superman.name,superman.superpowers,superman.life_points)
superman.attack()
superman.decrease_life(15)