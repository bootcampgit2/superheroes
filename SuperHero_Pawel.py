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

class superhero:
    def __init__(self,name,superpowers=[],life_points=0):
        self.name = name
        self.superpowers = ['ab', 'bc', 'cd']
        self.life_points = random.randint(1,10)
    def attack(self):
        x = random.randint(1,10)
        return x
    def decrease_life(self,x):
        self.life_points -= x


pawel = superhero('pawel')
###pawel.decrease_life(pawel.attack())
#print(pawel.life_points)
