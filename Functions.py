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
    Weapons = Choose([i.Name.lower() for i in WeaponOptions], "Choose Your Weapon:\n- Sword\n- Axe")
    for i in WeaponOptions:
        if Weapons == i.Name.lower():
            Weapons = i
    return Health, [Weapons]

def Fight(Attacker, Defender):
    print(f"{Attacker.Name}'s turn:")
    if Attacker.Name == "Player":
        while True:
            if Attacker.IsChargingAttack == False:
                Choice = Choose(["fight", "heal"], f"\nWhat will you do?\n- Fight\n- Heal ({Attacker.Flasks} flasks left)")
            else:
                Choice = Choose(["fight"], "\nThere is only one option.\n- Fight")
            if Choice == "heal":
                print("\nHealing...")
                sleep(0.5)
                Attacker.Heal()
                break
            elif Choice == "fight":
                Attacker.Attack(Defender)
                break
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

def FindSmallestNumber(Numbers: list):
    SmallestNumber = 99999
    for i in Numbers:
        if i < SmallestNumber:
            SmallestNumber = i
    return SmallestNumber

def Shop(Buyer, Inventory: list):
    print("\nGood day, Dear customer!\nHere are my wares:")
    for i in Inventory:
        print(f"- {i.Name} ({i.Cost} Gold)")
    print("")
    CheapestPrice = FindSmallestNumber([i.Cost for i in Inventory])
    while True:
        if Buyer.Gold < CheapestPrice:
            print("It appears you don't have enough money to buy anything...")
            break
        Item = Choose([i.Name.lower() for i in Inventory], f"What would you like to buy? (Gold: {Buyer.Gold})")
        for i in Inventory:
            if Item == i.Name.lower():
                Item = i
        if Buyer.Gold < Item.Cost:
            print(f"Sorry, but you don't have enough money to buy this. (You need {Item.Cost - Buyer.Gold} more Gold)")
        elif Item in Buyer.Weapons:
            print("It appears that you already have one of these...")
        else:
            print(f"\nPleasure doing business with you!\nObtained the {Item.Name}!")
            Buyer.Weapons.append(Item)
            Buyer.Gold -= Item.Cost
            break       
    sleep(1)
    print("Come again soon!")
    sleep(2)

Sword = Weapon("Sword", 20, 10, 1.5, 1, 0, 10)
Axe = Weapon("Axe", 15, 25, 2.4, 1, 0, 10)
BrokenSword = Weapon("Broken Sword", 2, 1, 1.5, 1, 0)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 0, 15)
Cleaver = Weapon("Cleaver", 12, 20, 2, 1, 2, 10)
Dagger = Weapon("Dagger", 8, 30, 1.75, 1, 2, 15)