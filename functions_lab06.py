# Import the random library to use for the dice later
import random


# Function to use loot and update health
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    if belt:
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            health_points = min(20, (health_points + 2))
            print(f"    |    You used {first_item} to up your health to {health_points}")
        elif first_item in bad_loot_options:
            health_points = max(0, (health_points - 2))
            print(f"    |    You used {first_item} to hurt your health to {health_points}")
        else:
            print(f"    |    You used {first_item} but it's not helpful")
    return belt, health_points


# Function to collect loot and update inventory
def collect_loot(loot_options, belt):
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt:", belt)
    return loot_options, belt


# Hero's Attack Function
def hero_attacks(combat_strength, m_health_points):
    print(f"    |    Player's weapon ({combat_strength}) ---> Monster ({m_health_points})")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength
        print(f"    |    You have reduced the monster's health to: {m_health_points}")
    return m_health_points


# Monster's Attack Function
def monster_attacks(m_combat_strength, health_points):
    print(f"    |    Monster's Claw ({m_combat_strength}) ---> Player ({health_points})")
    if m_combat_strength >= health_points:
        health_points = 0
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength
        print(f"    |    The monster has reduced Player's health to: {health_points}")
    return health_points


# Recursive Function for Dream Levels
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + inception_dream(num_dream_lvls - 1)


# Function to load previous game state
def load_game_state():
    try:
        with open("save.txt", "r") as file:
            lines = file.readlines()
            if lines:
                return lines[-1].strip()
    except FileNotFoundError:
        return None
    return None


# Function to save game outcome
def save_game_result(hero_won, num_stars):
    with open("save.txt", "a") as file:
        if hero_won:
            file.write(f"Hero has killed a monster and gained {num_stars} stars.\n")
        else:
            file.write("Monster has killed the hero previously.\n")
