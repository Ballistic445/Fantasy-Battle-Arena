from random import randint
class Character:
    Flasks = 3
    def __init__(self, Health, Weapons: list):
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
        if randint(0, 100) <= self.EquippedWeapon.CritChance:
            CritDamage = self.EquippedWeapon.CritDamage
        Target.Health -= self.EquippedWeapon.Damage * CritDamage

class Enemy(Character):
    def __init__(self, Name,  Health, Weapon):
            self.Health = Health
            self.Weapon = Weapon
            self.Name = Name

class Weapon:
    def __init__(self, Name,  Damage, CritChance, CritDamage, Cost = 0):
        self.Cost = Cost
        self.Damage = Damage
        self.CritChance = CritChance
        self.CritDamage = CritDamage
        self.Name = Name

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

Sword = Weapon("Sword", 20, 10, 1.5)
Axe = Weapon("Axe", 15, 25, 2.4)
BrokenSword = ("Broken Sword", 5, 1, 1.2)
