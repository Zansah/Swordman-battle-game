import random

# Define Swordsmen class
class Swordsman:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        damage = random.randint(1, self.attack_power)
        opponent.health -= damage
        print(f"{self.name} attacked {opponent.name} and dealt {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health})"


# Create swordsmen
player = Swordsman("Player", 100, 20)
enemy = Swordsman("Enemy", 100, 15)

# Game loop
while player.is_alive() and enemy.is_alive():
    print(player)
    print(enemy)
    print("------------------------------")
    print("1. Attack")
    print("2. Run")
    choice = input("Enter your choice: ")

    if choice == "1":
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)
    elif choice == "2":
        print("You ran away from the battle!")
        break
    else:
        print("Invalid choice!")

# Determine the winner
if player.is_alive():
    print("Congratulations! You defeated the enemy swordsman!")
else:
    print("You were defeated by the enemy swordsman. Better luck next time!")
