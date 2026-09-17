from time import sleep
from Classes import *

def Choose(Choices, Message):
    while True:
        out = input(f"{Message}\n> ")
        out = out.lower()
        if out in Choices:
            return out
        
def SetupCharacter():
    print("Fantasy Battle arena!\nCreate your character:\n ")
    Health = 100
    Weapons = Choose(["sword", "axe", "cleaver"], "Choose Your Weapon:\n- Sword\n- Axe\n- Cleaver")
    if Weapons == "sword":
        Weapons = Sword
    elif Weapons == "axe":
        Weapons = Axe
    elif Weapons == "cleaver":
        Weapons = Cleaver
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

