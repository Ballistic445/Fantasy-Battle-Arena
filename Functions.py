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
                Choice = Choose(["fight", "heal"], f"\nWhat will you do?\n- Fight\n- Heal ({Attacker.HealthFlasks.Count} flasks left)")
            else:
                Choice = Choose(["fight"], "\nThere is only one option.\n- Fight")
            if Choice == "heal":
                print("\nHealing...")
                sleep(0.5)
                Attacker.Heal()
                break
            elif Choice == "fight":
                if not Attacker.IsChargingAttack:
                    print("")
                    Attacker.EquippedWeapon.DisplayProfiles()
                    AttackProfiles = [i.Name.lower() for i in Attacker.EquippedWeapon.Profiles]
                    SelectedProfile = Choose(AttackProfiles, "How do you attack?")
                try:
                    for i in range(len(Attacker.EquippedWeapon.Profiles)):
                        if Attacker.EquippedWeapon.Profiles[i].Name.lower() == SelectedProfile:
                            Attacker.ProfileIndexStorage = i
                            Attacker.Attack(Defender, i)
                except UnboundLocalError:
                    Attacker.Attack(Defender, Attacker.ProfileIndexStorage)
                break
    else:
        sleep(1)
        ProfileIndex = randint(0, len(Attacker.EquippedWeapon.Profiles) - 1)
        try: 
            if Attacker.IsChargingAttack == False:
                Attacker.ProfileIndexStorage = ProfileIndex
            else:
                ProfileIndex = Attacker.ProfileIndexStorage
        except UnboundLocalError:
            pass
        Attacker.Attack(Defender, ProfileIndex)
    return Attacker.ProfileIndexStorage

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
        Options = [i.Name.lower() for i in Inventory]
        Options.append("exit")
        Item = Choose(Options, f"What would you like to buy? (Gold: {Buyer.Gold})\nYou can exit the shop by typing 'exit'")
        for i in Inventory:
            if Item == i.Name.lower():
                Item = i
        if Item == "exit":
            break
        if Buyer.Gold < Item.Cost:
            print(f"Sorry, but you don't have enough money to buy this. (You need {Item.Cost - Buyer.Gold} more Gold)")
        elif Item in Buyer.Weapons:
            print("It appears that you already have one of these...")
        else:
            print(f"\nPleasure doing business with you!\nObtained the {Item.Name}!")
            if Item.Name == "Health Flask":
                Buyer.HealthFlasks.Count += 1
                Buyer.HealthFlasks.MaxCount += 1
                Inventory[-1].Count -= 1
            else:
                Buyer.Weapons.append(Item)
            Buyer.Gold -= Item.Cost
            break       
    sleep(1)
    print("Come again soon!")
    sleep(2)

Sword = Weapon("Sword", [WeaponProfile("Strike", 20, 10, 1.5, 1, 0)], 10)
Axe = Weapon("Axe", [WeaponProfile("Strike", 15, 25, 2.4, 1, 0)], 10)
BrokenSword = Weapon("Broken Sword", [WeaponProfile("Strike", 2, 1, 1.5, 1, 0)], 0)
Hammer = Weapon("Hammer", [WeaponProfile("Strike", 25, 50, 2, 2, 0)], 15)
Cleaver = Weapon("Cleaver", [WeaponProfile("Strike", 12, 25, 2, 1, 3), WeaponProfile("Eviscerate", 20, 40, 1.5, 2, 4)], 10)
Dagger = Weapon("Dagger", [WeaponProfile("Strike", 8, 35, 1.75, 1, 4), WeaponProfile("Slash", 4, 50, 2, 1, 2)], 15)
Mace = Weapon("Mace", [WeaponProfile("Strike", 18, 10, 1.25, 1, 2), WeaponProfile("Bash", 30, 30, 1.4, 2, 3)], 15)
Greatsword = Weapon ("Greatsword", [WeaponProfile("Strike", 38, 30, 1.5, 2, 0), WeaponProfile("Sweep", 18, 20, 1.5, 1, 0)], 20)