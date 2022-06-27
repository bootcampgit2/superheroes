import random

from brancz_piotr_potwor import potwor
from hero_Kasia import my_hero
from SuperHero_Pawel import pawel
from potworek_kuby import super_potworek
from maciej_superpower import superman

superhero_list = [potwor,
                  my_hero,
                  pawel,
                  super_potworek,
                  superman,
                  ]

ans = ''
counter = 1
while (ans == '') & (len(superhero_list) > 1):
    print(f'----------RUNDA {counter}-------------')
    for hero in superhero_list:
        print(hero.name, hero.life_points)
    fighters = random.sample(superhero_list, k=2)
    attack = []
    for fighter in fighters:
        fighter_attack = fighter.attack()
        attack.append(fighter_attack)
        print(
            f'Postać {fighter.name} walczy {random.choice(fighter.superpowers)} i zadaje {fighter_attack} obrazeń')

    if attack[0] > attack[1]:
        attack_points = attack[0] - attack[1]
        print(
            f'Postac {fighters[0].name} wygrywa z {fighters[1].name} zadajac mu {attack_points} obrazen')
        fighters[1].decreas_life(attack_points)
        if fighters[1].life_points <= 0:
            print(f'Postac {fighters[1].name} umiera')
            superhero_list.remove(fighters[1])

    elif attack[0] < attack[1]:
        attack_points = attack[1] - attack[0]
        print(
            f'Postac {fighters[1].name} wygrywa z {fighters[0].name} zadajac mu {attack_points} obrazen')
        fighters[0].decreas_life(attack_points)
        if fighters[0].life_points <= 0:
            print(f'Postac {fighters[0].name} umiera')
            superhero_list.remove(fighters[0])

    else:
        print('REMIS')
        counter += 1
        continue
    counter += 1
    ans = input()

print(f'Wygrywa: {superhero_list[0].name}')
