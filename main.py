from FunctionsAndClasses import *

Health, Weapons = SetupCharacter()
Player = Character(Health, Weapons)
Hollow = Enemy("Hollow", 30, [BrokenSword])

print(f"Health: {Player.Health}")
print(f"Weapons: {Player.Weapons[0].Name}")

while Player.Health > 0 and Hollow.Health > 0:
    Choice = Choose(["fight", "heal"], f"What will you do?\n- Fight\n- Heal ({Player.Flasks} flasks left)")
    if Choice == "heal":
        Player.Heal()
    elif Choice == "fight":
        Player.Attack(Hollow)
        print(Hollow.Health)