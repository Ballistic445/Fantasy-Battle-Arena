from Functions import *
from Classes import *
from sys import exit

Health, Weapons = SetupCharacter()
Player = Character(Health, Weapons, "Player")
Hollow = Enemy("Hollow", 35, BrokenSword)
Soldier = Enemy("Soldier", 75, Hammer)

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
