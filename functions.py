import random

def collect_loot(belt, loot_options):
    print("!!You find a loot bag!!")
    for _ in range(2):
        input("Roll for loot (Press enter)")
        loot = random.choice(loot_options)
        loot_options.remove(loot)
        belt.append(loot)
    belt.sort()
    print("Your belt:", belt)
    return belt, loot_options

def use_loot(belt, health_points, good_loot_options, bad_loot_options):
    if belt:
        first_item = belt.pop(0)
        if first_item in good_loot_options:
            health_points = min(6, health_points + 2)
        elif first_item in bad_loot_options:
            health_points = max(0, health_points - 2)
        print(f"You used {first_item}. Current health: {health_points}")
    return belt, health_points

def hero_attacks(combat_strength, m_health_points):
    attack_damage = random.randint(1, combat_strength)
    m_health_points = max(0, m_health_points - attack_damage)
    print(f"Hero attacks! Monster health is now {m_health_points}")
    return m_health_points

def monster_attacks(m_combat_strength, health_points):
    attack_damage = random.randint(1, m_combat_strength)
    health_points = max(0, health_points - attack_damage)
    print(f"Monster attacks! Hero health is now {health_points}")
    return health_points
