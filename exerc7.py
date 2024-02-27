import random

class Character:
    def __init__(self, name, life):
        self.name = name
        self.life = life

class Warrior(Character):
    def attack(self, enemy: Character) -> None:
        damage = random.randint(10, 20)
        enemy.life -= damage
        print(f"{self.name} attacks {enemy.name} and causes {damage} damage. {enemy.name} has {enemy.life} life left.")



character1 = Warrior("Warrior 1", 100)
character2 = Warrior("Character 2", 100)

while character1.life > 0 and character2.life > 0:
    character1.attack(character2)
    character2.attack(character1)
    
if character1.life > 0:
    print(f"{character1.name} wins!")

elif character2.life > 0:
    print(f"{character2.name} wins!")

else:
    print("It's a draw!")
