from Functions import *
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
        Damage = self.bleed * 2
        if self.bleed >= 5:
            print(f"{self.Name} bursts out in blood, losing 20 HP")
            self.bleed %= 5
            Damage = 20
        elif self.bleed > 0:
            print(f"{self.Name} bleeds out, losing {Damage} HP.")
            self.bleed -= 1
        self.Health -= Damage

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

Sword = Weapon("Sword", 20, 10, 1.5, 1, 0, 10)
Axe = Weapon("Axe", 15, 25, 2.4, 1, 0, 10)
BrokenSword = Weapon("Broken Sword", 5, 1, 1.2, 1, 0)
Hammer = Weapon("Hammer", 25, 50, 2, 2, 0, 15)
Cleaver = Weapon("Cleaver", 12, 20, 2, 1, 2, 15)
