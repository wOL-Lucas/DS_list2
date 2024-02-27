import random

def throw_dice():
    return random.randint(1,6)



dices = [throw_dice() for i in range(20)]
for i in range(1,7):
    print(f"Number of {i}: {dices.count(i)}")
