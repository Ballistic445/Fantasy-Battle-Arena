from Classes import *
from Functions import *
from sys import exit

Health, Weapons = SetupCharacter([Sword, Axe])
Player = Character(Health, Weapons, "Player")
Undead = Enemy("Hollow", 35, BrokenSword, 5)
Soldier = Enemy("Soldier", 75, Hammer, 10)
Assassin = Enemy("Assassin", 100, Dagger, 20)
Knight = Enemy("Knight", 125, Greatsword, 30)
ShopFlasks = Flask(5, Player.HealthFlasks.Potency, 5, "Health Flask")

Enemies = [Undead, Soldier, Assassin, Knight]

print("\nGet ready...")
sleep(2.5)

x = 1
for i in Enemies:
    if x % 4 == 0:
        print("Flasks Replenished!")
        Player.HealthFlasks.Count = Player.HealthFlasks.MaxCount 
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
        Decision = Choose(["hunt", "shop", "inv"], "\nwhat would You like to do next?\n- Hunt down another enemy (Type 'hunt')\n- Go to the shop (Type 'shop')\n- View weapon inventory (Type 'inv')") 
        if Decision == "shop":
            print("\nEntering the shop...")
            sleep(1)
            Shop(Player, [Sword, Axe, Cleaver, Hammer, Dagger, Mace, ShopFlasks])
        elif Decision == "inv":
            Player.DisplayWeaponInventory()
            if Choose(["y", "n"], "Would you like to change your equipped weapon? (y/n)") == "y":
                NewEquippedWeapon = Choose([i.Name.lower() for i in Player.Weapons], "Enter the name of the weapon you want to equip")
                for i in Player.Weapons:
                    if NewEquippedWeapon == i.Name.lower():
                        Player.EquippedWeapon = i
                        print(f"You have equipped the {i.Name}!")
                        sleep(1)
        else:
            print("\nThe next enemy approaches...")
            break
    sleep(2)
    x += 1

print("\nYou won!")