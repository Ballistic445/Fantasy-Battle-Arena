from random import randint
from time import sleep

class Flask:
    def __init__(self, Count, Potency, Cost, Name):
        self.Count = Count
        self.MaxCount = Count
        self.Potency = Potency
        self.Cost = Cost
        self.Name = Name

class Character:
    ChargeTimer = 1
    IsChargingAttack = False
    bleed = 0
    Gold = 0
    HealthFlasks = Flask(3, 40, 0, "Health Flask")
    def __init__(self, Health, Weapons: list, Name):
        self.Name = Name
        self.Health = Health
        self.MaxHealth = Health
        self.Weapons = Weapons
        self.EquippedWeapon = self.Weapons[0]

    def Heal(self):
        if self.HealthFlasks.Count > 0:
            self.Health += self.HealthFlasks.Potency
            self.HealthFlasks.Count -= 1
        else:
            print("No Flasks Left")
            return 0
        if self.Health > 100: self.Health = 100

    def Attack(self, Target):
        print("")
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
            self.IsChargingAttack = False
        else:
            print(f"{self.Name} is Charging up an attack...")
            self.ChargeTimer += 1
            self.IsChargingAttack = True
        sleep(0.8)

    def Bleed(self):
        Damage = self.bleed * 2
        if self.bleed >= 5:
            print(f"{self.Name} bursts out in blood, losing 15 HP")
            self.bleed %= 5
            Damage = 15
        elif self.bleed > 0:
            print(f"{self.Name} bleeds out, losing {Damage} HP.")
            self.bleed -= 1
        self.Health -= Damage

    def DisplayHealth(self):
        print(f"{self.Name}'s HP: {self.Health}/{self.MaxHealth}")

    def DisplayWeaponInventory(self):
        print("\nCurrently owned weapons: ")
        for i in self.Weapons:
            print(f"- {i.Name}")
        print(f"Equipped weapon: {self.EquippedWeapon.Name}")

class Enemy(Character):
    def __init__(self, Name, Health, Weapon, Gold):
            self.Health = Health
            self.MaxHealth = Health
            self.EquippedWeapon = Weapon
            self.Name = Name
            self.Gold = Gold

class Weapon:
    def __init__(self, Name,  Damage, CritChance, CritDamage, ChargeTime, Bleed, Cost = 0):
        self.Cost = Cost
        self.Damage = Damage
        self.CritChance = CritChance
        self.CritDamage = CritDamage
        self.Name = Name
        self.ChargeTime = ChargeTime
        self.Bleed = Bleed