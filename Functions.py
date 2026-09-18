from time import sleep
from Classes import *

def Choose(Choices, Message):
    while True:
        out = input(f"{Message}\n> ")
        out = out.lower()
        if out in Choices:
            return out
        
def SetupCharacter(WeaponOptions):
    print("Fantasy Battle arena!\nCreate your character:\n ")
    Health = 100
    Weapons = Choose(["sword", "axe", "cleaver"], "Choose Your Weapon:\n- Sword\n- Axe\n- Cleaver")
    for i in WeaponOptions:
        if Weapons == i.Name.lower():
            Weapons = i
    return Health, [Weapons]

def Fight(Attacker, Defender):
    print(f"{Attacker.Name}'s turn:")
    if Attacker.Name == "Player":
        Choice = Choose(["fight", "heal"], f"\nWhat will you do?\n- Fight\n- Heal ({Attacker.Flasks} flasks left)")
        if Choice == "heal":
            print("\nHealing...")
            sleep(0.5)
            Attacker.Heal()
        elif Choice == "fight":
            Attacker.Attack(Defender)
    else:
        sleep(1)
        Attacker.Attack(Defender)

def Combat(Player, Opponent):
    while Player.Health > 0 and Opponent.Health > 0:
        print("\n")
        Player.Bleed()
        Opponent.Bleed()
        Player.DisplayHealth()
        Opponent.DisplayHealth()
        if Opponent.Health > 0 and Player.Health > 0:
            Fight(Player, Opponent)
        if Opponent.Health > 0 and Player.Health > 0:
            Fight(Opponent, Player)
    if Player.Health > 0:
        return True
    else: return False

def Shop(Buyer, Inventory: list):
    #show buyer wares
    #allow buyer to choose
    #give item to buyer
    #loop until cant buy anything else or exits
    pass

Sword = Weapon("Sword", 20, 10, 1.5, 1, 0, 10)
Axe = Weapon("Axe", 15, 25, 2.4, 1, 0, 10)
BrokenSword = Weapon("Broken Sword", 2, 1, 1.5, 1, 0)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 0, 15)
Cleaver = Weapon("Cleaver", 12, 20, 2, 1, 2, 10)
Dagger = Weapon("Dagger", 8, 25, 1.75, 1, 2, 15)