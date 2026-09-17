from random import randint
from time import sleep
class Character:
    Flasks = 3
    ChargeTimer = 1
    bleed = 0
    def __init__(self, Health, Weapons: list, Name):
        self.Name = Name
        self.Health = Health
        self.MaxHealth = Health
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
        InflictsBleed = 0
        if self.EquippedWeapon.ChargeTime == self.ChargeTimer:
            if randint(0, 100) <= self.EquippedWeapon.CritChance:
                CritDamage = self.EquippedWeapon.CritDamage
                InflictsBleed = self.EquippedWeapon.Bleed * 2
                print("Critical Hit!")
                sleep(0.5)
            elif randint(0, 100) <= self.EquippedWeapon.CritChance * 2:
                InflictsBleed = self.EquippedWeapon.Bleed
            Target.Health -= self.EquippedWeapon.Damage * CritDamage
            Target.bleed += InflictsBleed
            print(f"{self.Name} deals {self.EquippedWeapon.Damage * CritDamage} damage!")
            self.ChargeTimer = 1
        else:
            print(f"{self.Name} is Charging up an attack...")
            self.ChargeTimer += 1
        sleep(0.8)

    def Bleed(self):
        Damage = self.bleed * 3
        if self.bleed >+ 5:
            print(f"{self.Name} bursts out in blood, losing 25 HP")
            self.bleed %= 5
        elif self.bleed > 0:
            print(f"{self.Name} bleeds out, losing {Damage} HP.")
            self.Health -= Damage
            self.bleed -= 1

    def DisplayHealth(self):
        print(f"{self.Name}'s HP: {self.Health}/{self.MaxHealth}")

class Enemy(Character):
    def __init__(self, Name,  Health, Weapon):
            self.Health = Health
            self.MaxHealth = Health
            self.EquippedWeapon = Weapon
            self.Name = Name

class Weapon:
    def __init__(self, Name,  Damage, CritChance, CritDamage, ChargeTime, Bleed, Cost = 0):
        self.Cost = Cost
        self.Damage = Damage
        self.CritChance = CritChance
        self.CritDamage = CritDamage
        self.Name = Name
        self.ChargeTime = ChargeTime
        self.Bleed = Bleed

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
        Fight(Player, Opponent)
        if Opponent.Health > 0:
            Fight(Opponent, Player)
    if Player.Health > 0:
        return True
    else: return False

Sword = Weapon("Sword", 20, 10, 1.5, 1, 0, 10)
Axe = Weapon("Axe", 15, 25, 2.4, 1, 0, 10)
BrokenSword = Weapon("Broken Sword", 5, 1, 1.2, 1, 0)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 0, 15)
Cleaver = Weapon("Cleaver", 12, 20, 2, 1, 1, 15)