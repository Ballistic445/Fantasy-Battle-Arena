from Classes import *
from Functions import *
from sys import exit

Health, Weapons = SetupCharacter([Sword, Axe, Cleaver])
Player = Character(Health, Weapons, "Player")
Hollow = Enemy("Hollow", 35, BrokenSword, 5)
Soldier = Enemy("Soldier", 75, Hammer, 10)
Assassin = Enemy("Assassin", 100, Dagger)

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