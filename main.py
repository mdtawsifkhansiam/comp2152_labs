import random
import function
import sys

# Game Flow
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

num_stars = 0
input_valid = False

i = 0
while not input_valid and i in range(5):
    try:
        combat_strength = int(input("Enter your combat Strength (1-6): "))
        if combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only")
        input_valid = True
    except ValueError as e:
        print(e)
        i += 1

m_input_valid = False
while not m_input_valid and i in range(5):
    try:
        m_combat_strength = int(input("Enter the monster's combat Strength (1-6): "))
        if m_combat_strength not in range(1, 7):
            raise ValueError("Enter a valid integer between 1 and 6 only")
        m_input_valid = True
    except ValueError as e:
        print(e)
        i += 1

if input_valid and m_input_valid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("Player rolled " + str(health_points) + " health points")

input("Roll the dice for the monster's combat strength (Press enter)")
m_combat_strength = random.choice(small_dice_options)
print("Player rolled " + str(m_combat_strength) + " combat strength for the monster")

input("Roll the dice for the monster's health points (Press enter)")
m_health_points = random.choice(big_dice_options)
print("Player rolled " + str(m_health_points) + " health points for the monster")

while m_health_points > 0 and health_points > 0:
    input("Roll to see who attacks first (Press Enter)")
    attack_roll = random.choice(small_dice_options)
    if not (attack_roll % 2 == 0):
        input("You strike (Press enter)")
        m_health_points = function.hero_attacks(combat_strength, m_health_points)
        if m_health_points != 0:
            input("The monster strikes (Press enter)!!!")
            try:
                health_points = function.monster_attacks(m_combat_strength, health_points)
            except Exception as e:
                print(f"Error during monster's attack: {e}")
    else:
        input("The Monster strikes (Press enter)")
        try:
            health_points = function.monster_attacks(m_combat_strength, health_points)
        except Exception as e:
            print(f"Error during monster's attack: {e}")
        if health_points != 0:
            input("The hero strikes!! (Press enter)")
            m_health_points = function.hero_attacks(combat_strength, m_health_points)

# Test case from instruction
# Uncomment this to test the exception handling
# health_points = function.monster_attacks("Somestring1", "Somestring2")
