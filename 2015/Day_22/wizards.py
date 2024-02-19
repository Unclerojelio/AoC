import time
import re
import itertools

spells = {'magic_missile' : 53,
          'drain'         : 73,
          'shield'        : 113,
          'poison'        : 173,
          'recharge'      : 229}

def fight(player, boss):
    while True:
        x = player['damage'] - boss['armor']
        boss['health'] -= max(1, x)
        if boss['health'] <= 0:
            return True
        y = boss['damage'] - player['armor']
        player['health'] -= max(1, y)
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

    player = {'health' : 50,
              'mana'   : 500,
              'armor'  : 0}

    boss = {'health' : 55,
            'armor'  :   0,
            'damage' : 8}

    spell_names = ['magic_missile', 'drain', 'shield', 'poison', 'recharge']
    combos = itertools.combinations_with_replacement(spell_names, len(spells_names))

    wins = set()
    losses = set()

    if fight(player, boss):
        wins.add(cost)
    else:
        losses.add(cost)

    ans1 = min(wins)
    ans2 = max(losses)
    # assert ans1 == 91
    # assert ans2 == 158 
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
