from FunctionsAndClasses import *

Health, Weapons = SetupCharacter()
Player = Character(Health, Weapons, "Player")
Hollow = Enemy("Hollow", 35, [BrokenSword])

print(f"Health: {Player.Health}")
print(f"Weapons: {Player.Weapons[0].Name}")

while Player.Health > 0 and Hollow.Health > 0:
    print("\n")
    Player.DisplayHealth()
    Hollow.DisplayHealth()
    Choice = Choose(["fight", "heal"], f"\nWhat will you do?\n- Fight\n- Heal ({Player.Flasks} flasks left)")
    if Choice == "heal":
        print("\nHealing...")
        Player.Heal()
    elif Choice == "fight":
        Player.Attack(Hollow)

print("You won!")