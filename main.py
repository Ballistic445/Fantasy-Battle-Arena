from Functions import *
from Classes import *
from sys import exit

Sword = Weapon("Sword", 20, 10, 1.5, 1, 0, 10)
Axe = Weapon("Axe", 15, 25, 2.4, 1, 0, 10)
BrokenSword = Weapon("Broken Sword", 2, 1, 1.5, 1, 0)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 0, 15)
Cleaver = Weapon("Cleaver", 12, 20, 2, 1, 2, 15)
Dagger = Weapon("Dagger", 8, 35, 2, 1, 2, 10)

Health, Weapons = SetupCharacter()
Player = Character(Health, Weapons, "Player")
Hollow = Enemy("Hollow", 35, BrokenSword)
Soldier = Enemy("Soldier", 75, Hammer)
Assassin = Enemy("Assassin", 125, Dagger)

print(f"\nHealth: {Player.Health}")
print(f"Weapons: {Player.Weapons[0].Name}")
sleep(1)

if Combat(Player, Hollow):
    print("You won!")
else: 
    print("You died... :(")
    exit()

sleep(2)

if Combat(Player, Soldier):
    print("You won!")
else: 
    print("You died... :(")
    exit()

sleep(2)

if Combat(Player, Assassin):
    print("You won!")
else: 
    print("You died... :(")
    exit()