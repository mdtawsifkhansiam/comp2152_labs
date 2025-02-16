# Import the random library to use for the dice later
import random
import os

# Import functions from another file
import functions_lab06

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define Monster's Powers
monster_powers = {"Fire Magic": 2, "Freeze Time": 4, "Super Hearing": 6}

# Initialize combat strength values
combat_strength = 1
m_combat_strength = 1
num_stars = 0

# Load previous game result
if os.path.exists("save.txt"):
    with open("save.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            if "Hero" in last_line and "stars" in last_line:
                num_stars = int(last_line.split()[-2])
                if num_stars > 3:
                    m_combat_strength += 1
            elif "Monster" in last_line:
                combat_strength += 1

# Get valid input for Hero and Monster's Combat Strength
while True:
    combat_strength_input = input("Enter your combat Strength (1-6): ")
    m_combat_strength_input = input("Enter the monster's combat Strength (1-6): ")
    if combat_strength_input.isdigit() and m_combat_strength_input.isdigit():
        combat_strength, m_combat_strength = int(combat_strength_input), int(m_combat_strength_input)
        if 1 <= combat_strength <= 6 and 1 <= m_combat_strength <= 6:
            break
    print("Invalid input. Enter numbers between 1 and 6.")

# Roll for weapon
weapon_roll = random.choice(small_dice_options)
combat_strength = min(6, combat_strength + weapon_roll)
print(f"The hero's weapon is {weapons[weapon_roll - 1]}")

# Roll for health points
health_points = random.choice(big_dice_options)
m_health_points = random.choice(big_dice_options)

# Collect Loot
total_loot = 2
for _ in range(total_loot):
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)
belt.sort()

# Use Loot
belt, health_points = functions_lab06.use_loot(belt, health_points)

# Validate Dream Level Input
while True:
    num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
    if num_dream_lvls.isdigit():
        num_dream_lvls = int(num_dream_lvls)
        if 0 <= num_dream_lvls <= 3:
            break
    print("Invalid input. Enter a number between 0 and 3.")

if num_dream_lvls != 0:
    health_points -= 1
    crazy_level = functions_lab06.inception_dream(num_dream_lvls)
    combat_strength += crazy_level

# Fight Sequence
while m_health_points > 0 and health_points > 0:
    attack_roll = random.choice(small_dice_options)
    if attack_roll % 2 != 0:
        m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
        else:
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
            num_stars = 1 if health_points == 0 else 2
    else:
        health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            num_stars = 1
        else:
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
            num_stars = 3 if m_health_points == 0 else 2

# Save Game Outcome
with open("save.txt", "a") as file:
    if m_health_points == 0:
        file.write(f"Hero has killed a monster and gained {num_stars} stars.\n")
    else:
        file.write("Monster has killed the hero previously.\n")
