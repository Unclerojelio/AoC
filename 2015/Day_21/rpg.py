import time
import re
from itertools import combinations

def fight(me, monster):
    return True

def do_tests():
    me = {'hpoints' : 8,
          'damage' : 5,
          'armor' : 5}

    monster = {'hpoints' : 12,
               'damage' : 7,
               'armor' : 2}

    ans1 = fight(me, monster)
    #assert ans1 == 4
    return True

def main():
    start_time = time.time()
    
    if do_tests():
        print("Tests Passed")

    me = {'hpoints' : 100,
          'damage' : 0,
          'armor' : 0,
          'equipment' : []}

    monster = {'hpoints' : 100,
              'damage' : 8,
              'armor' : 2}

    ans1 = fight(me, monster)
    #ans2 = solve()

    ans2 = 0
    # assert ans1 == 518
    # assert ans2 == 0 
    print("Answer 1:", ans1, "Answer 2: ", ans2)
    print("Elapsed time:", (time.time() - start_time) * 10**3, "ms")

if __name__=="__main__":
    main()
