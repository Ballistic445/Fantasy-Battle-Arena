from Classes import *
from Functions import *
from sys import exit

Health, Weapons = SetupCharacter([Sword, Axe])
Player = Character(Health, Weapons, "Player")
Hollow = Enemy("Hollow", 35, BrokenSword, 5)
Soldier = Enemy("Soldier", 75, Hammer, 10)
Assassin = Enemy("Assassin", 100, Dagger, 20)

Enemies = [Hollow, Soldier, Assassin]

print(f"\nHealth: {Player.Health}")
print(f"Weapons: {Player.Weapons[0].Name}")
sleep(1)

for i in Enemies:
    if Combat(Player, i):
        print("Enemy Defeated!")
        print(f"You have earned {i.Gold} Gold.")
        Player.Gold += i.Gold
        if i == Enemies[-1]:
            sleep(2)
            break
    else: 
        print("You died... :(")
        exit()
    sleep(0.5)
    while True:
        Decision = Choose(["hunt", "shop"], "\nwhat would You like to do next?\n- Hunt down another enemy (Type 'hunt')\n- Go to the shop (Type 'shop')") 
        if Decision == "shop":
            print("\nEntering the shop...")
            sleep(1)
            Shop(Player, [Sword, Axe, Cleaver, Hammer, Dagger])
        else:
            print("The next enemy approaches...")
            break
    sleep(2)

print("You won!")