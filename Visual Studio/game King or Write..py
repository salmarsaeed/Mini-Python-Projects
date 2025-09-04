#import random
#print("Welcome to the game, King or Write.")
#input("Press Enter")
#cump_rand=random.random()
#if cump_rand>=0.5:
#    print("King👑")
#else:
#    print("Wrinte🪶")



import random
print("Welcome to the game, King or Write.")
input("Press Enter")
cump_rand=random.randint(0,1)
if cump_rand==0:
    print("King👑")
else:
    print("Wrinte🪶")