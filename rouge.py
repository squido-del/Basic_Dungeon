import random

player = {
    "health": 120,
    "gold": 40,
    "potions": 1,
    "fire_potions": 0,
    "artifact": False
}

room_number = 1

while room_number <= 10 and player["health"] > 0:
    print(f"\n--- Room {room_number} ---")
    print(f"Health: {player['health']} | Gold: {player['gold']} | Potions: {player['potions']}")

    event = random.choice(["enemy", "treasure", "trap", "merchant"])

    # ENEMY EVENT
    if event == "enemy":
        print("⚔️ You encountered an enemy!")
        damage = random.randint(10, 25)
        player["health"] -= damage
        print(f"The enemy hit you for {damage} damage.")

    # TREASURE EVENT
    elif event == "treasure":
        print("💰 You found treasure!")
        gold_found = random.randint(15, 40)
        player["gold"] += gold_found
        print(f"You gained {gold_found} gold.")

    # TRAP EVENT
    elif event == "trap":
        print("🪤 You triggered a trap!")
        damage = random.randint(5, 20)
        player["health"] -= damage
        print(f"You lost {damage} health.")

        risk = input("Do you want to take a risky gamble? (yes/no): ").lower()

        if risk == "yes":
            gamble = random.choice(["treasure", "trap"])
            if gamble == "treasure":
                print("Lucky! You found bonus treasure!")
                player["gold"] += 50
            elif gamble == "trap":
                print("Bad luck! Another trap!")
                player["health"] -= 30
        else:
            print("You avoided further danger.")

    # MERCHANT EVENT (FIXED INDENTATION)
    elif event == "merchant":
        print("🧙 Merchant Shop")
        print("1. Potion (heal 20) - 30 gold")
        print("2. Fire Potion (extra boss damage) - 50 gold")
        print("3. Artifact (boss special item) - 80 gold")
        print("4. Leave")

        choice = input("Choose item (1-4): ")

        if choice == "1" and player["gold"] >= 30:
            player["gold"] -= 30
            player["potions"] += 1
            print("You bought a potion.")

        elif choice == "2" and player["gold"] >= 50:
            player["gold"] -= 50
            player["fire_potions"] += 1
            print("You bought a fire potion.")

        elif choice == "3" and player["gold"] >= 80:
            player["gold"] -= 80
            player["artifact"] = True
            print("You bought the mysterious artifact.")

        else:
            print("Not enough gold or invalid choice.")

    # Death check
    if player["health"] <= 0:
        print("\n💀 You died in the dungeon...")
        break

    room_number += 1

# ---------------- BOSS ROUND AFTER LOOP ---------------- #

if player["health"] > 0:
    print("\n______BOSS ROUND______")
    print("👹___THE MONSTER HAS ENTERED___👹")

    boss_health = 100

    while boss_health > 0 and player["health"] > 0:

        boss_powers = random.randint(1, 10)

        if boss_powers == 1:
            print("Boss has died instantly 😱!!!")
            boss_health = 0

        elif boss_powers == 2:
            damage = random.randint(5, 20)
            player["health"] -= damage
            print(f"Boss attacked you for {damage} damage!")

        elif boss_powers == 3:
            if player["fire_potions"] > 0:
                print("🔥 You used fire potion!")
                boss_health -= 60
                player["fire_potions"] -= 1
            else:
                print("No fire potions left!")

        elif boss_powers == 4:
            if player["artifact"]:
                print("You used artifact...")
                print("You were tricked! Boss gained more health!")
                boss_health += 100
                player["artifact"] = False
            else:
                print("No artifact to use!")

        elif boss_powers == 5:
            damage = random.randint(1, 20)
            boss_health -= damage
            print(f"You struck the boss for {damage} damage!")

        elif boss_powers == 6:
            print("Boss became a statue!")
            take_risk = input("Want to take risk yes/no: ").lower()

            if take_risk == "yes":
                boss_health -= 30
                print("You dealt 30 damage!")
            else:
                boss_health += 20
                print("Boss absorbed energy and gained 20 health!")

        elif boss_powers == 7:
            print("The boss sent minions!")
            minion_powers = random.randint(1, 2)

            if minion_powers == 1:
                print("You defeated the minion quickly!")
            else:
                print("You turned the minion against the boss!")
                boss_health -= 20

        elif 8 <= boss_powers <= 10:
            print("✨ The boss energy backfires!")
            player["health"] += 50
            print("You gained 100 health!")

        print(f"Boss Health: {boss_health}")
        print(f"Player Health: {player['health']}")
    if boss_health==0:
        print("YOU WON!!!")
        print("YOU SURVIVED THE MAZE🥳🙌")    
