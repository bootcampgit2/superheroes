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
# import superman from zadanie_supe




import random

class Potwor:
    def __init__(self, name, superpower, life_points)
        self.name = name
        self.name = superpower
        self.life_points = life_points




    def attack(selfself):
        return random.randint(1,10)
    def decrease_life(self,x):
        self.life_points -= x

super_ciastko = SuperCiastko('supercistko', ["raz", "dwa" , "trzy"])
print(super_ciastko.attack())
