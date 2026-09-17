from random import randint
from time import sleep
class Character:
    Flasks = 3
    ChargeTimer = 1
    def __init__(self, Health, Weapons: list, Name):
        self.Name = Name
        self.Health = Health
        self.Weapons = Weapons
        self.EquippedWeapon = self.Weapons[0]

    def Heal(self):
        if self.Flasks > 0:
            self.Health += 40
            self.Flasks -= 1
        else:
            print("No Flasks Left")
            return 0
        if self.Health > 100: self.Health = 100

    def Attack(self, Target):
        CritDamage = 1
        if self.EquippedWeapon.ChargeTime == self.ChargeTimer:
            if randint(0, 100) <= self.EquippedWeapon.CritChance:
                CritDamage = self.EquippedWeapon.CritDamage
                print("Critical Hit!")
                sleep(0.5)
            Target.Health -= self.EquippedWeapon.Damage * CritDamage
            print(f"{self.Name} deals {self.EquippedWeapon.Damage * CritDamage} damage!")
            self.ChargeTimer = 1
        else:
            print(f"{self.Name} is Charging up an attack...")
            self.ChargeTimer += 1
        sleep(0.8)

    def DisplayHealth(self):
        print(f"{self.Name}'s HP: {self.Health}")

class Enemy(Character):
    def __init__(self, Name,  Health, Weapon):
            self.Health = Health
            self.EquippedWeapon = Weapon
            self.Name = Name

class Weapon:
    def __init__(self, Name,  Damage, CritChance, CritDamage, ChargeTime, Cost = 0):
        self.Cost = Cost
        self.Damage = Damage
        self.CritChance = CritChance
        self.CritDamage = CritDamage
        self.Name = Name
        self.ChargeTime = ChargeTime

def Choose(Choices, Message):
    while True:
        out = input(f"{Message}\n> ")
        out = out.lower()
        if out in Choices:
            return out
        
def SetupCharacter():
    print("Fantasy Battle arena!\nCreate your character:\n ")
    Health = 100
    Weapons = Choose(["sword", "axe"], "Choose Your Weapon:\n- Sword\n- Axe")
    if Weapons == "sword":
        Weapons = Sword
    elif Weapons == "axe":
        Weapons = Axe
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
        Player.DisplayHealth()
        Opponent.DisplayHealth()
        Fight(Player, Opponent)
        if Opponent.Health > 0:
            Fight(Opponent, Player)
    if Player.Health > 0:
        return True
    else: return False

Sword = Weapon("Sword", 20, 10, 1.5, 1)
Axe = Weapon("Axe", 15, 25, 2.4, 1)
BrokenSword = Weapon("Broken Sword", 5, 1, 1.2, 1)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 15)