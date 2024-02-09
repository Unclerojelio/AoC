import time
import re
from itertools import product

'''
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''

weapons = {'dagger' : (8,4,0),
           'shortsword' : (10,5,0),
           'warhammer' : (25,6,0),
           'longsword' : (40,7,0),
           'greataxe' : (74,8,0)}

armors = {'leather' : (13,0,1),
          'chainmail' : (31,0,2),
          'splintmail' : (53,0,3),
          'bandedmail' : (75,0,4),
          'platemail' : (102,0,5)}

rings = {'damage1' : (25,1,0),
         'damage2' : (50,2,0),
         'damage3' : (100,3,0),
         'defense1' : (20,0,1),
         'defense2' : (40,0,2),
         'defense3' : (80,0,3)}

def find_unique_combinations(weapons, armors, rings):
    combinations = []

    weapon_list = list(weapons.keys())
    armor_list = list(armors.keys())
    ring_list = list(rings.keys())

    for weapon in weapon_list:
        for armor in [None] + armor_list:
            for ring in [None] + ring_list + [ring_list[i:i+2] for i in range(len(ring_list))]:
                combinations.append((weapon, armor, ring))
    return combinations

def fight(player, boss):
    while True:
        x = player['damage'] - boss['armor']
        boss['health'] -= x
        if boss['health'] <= 0:
            return True
        y = boss['damage'] - player['armor']
        player['health'] -= y
        if player['health'] <= 0:
            return False

def do_tests():
    player = {'health' : 8,
          'damage' : 5,
          'armor' : 5}

    boss = {'health' : 12,
               'damage' : 7,
               'armor' : 2}

    ans1 = fight(player, boss)
    #assert ans1 == 4
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    player = {'health' : 100,
          'damage' : 0,
          'armor' : 0,
          'equipment' : []}

    boss = {'health' : 100,
              'damage' : 8,
              'armor' : 2}

    wins = set()
    losses = set()
    unique_combinations = find_unique_combinations(weapons, armors, rings)
    for combination in unique_combinations:
        cost = 0
        damage = 0
        armor = 0
        for item in combination:
            if isinstance(item, list):
                for ring in item:
                    cost += rings[ring][0]
                    damage += rings[ring][1]
                    armor += rings[ring][2]
            elif item in weapons:
                cost += weapons[item][0]
                damage += weapons[item][1]
                armor += weapons[item][2]
            elif item in armors:
                cost += armors[item][0]
                damage += armors[item][1]
                armor += armors[item][2]
            elif item in rings:
                cost += rings[item][0]
                damage += rings[item][1]
                armor += rings[item][2]
        player['health'] = 100
        player['damage'] = damage
        player['armor'] = armor
        boss['health'] = 100
        if fight(player, boss):
            wins.add(cost)
        else:
            losses.add(cost)

    ans1 = min(wins)
    ans2 = max(losses)
    assert ans1 == 91
    # assert ans2 == 0 
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
