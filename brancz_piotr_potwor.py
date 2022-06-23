import random
class Straszny_potwor:
        def __init__(self, name):
            self.name = name

        def attack (atak_liczba):
            atak_liczba=random.randint(1,10)

        def decrease_life (zmniejszenie_zycia):
            zmniejszenie_zycia=int(input("o ile zmniejszyc zycie?"))



potwor= Straszny_potwor()