import random

monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

monster_power = random.choice(list(monster_powers.keys()))
print(f"Monster rolled power: {monster_power}")

m_combat_strength = random.randint(1, 6)
m_combat_strength = min(6, m_combat_strength + monster_powers[monster_power])
print(f"Updated Monster Combat Strength: {m_combat_strength}")

belt = []
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
good_loot_options = ["Health Potion", "Leather Boots"]
bad_loot_options = ["Poison Potion"]

print("Player has found a loot bag!")
for _ in range(2):
    input("Press Enter to roll for loot...")
    loot_item = random.choice(loot_options)
    loot_options.remove(loot_item)
    belt.append(loot_item)
    print(f"Added {loot_item} to belt: {belt}")

print("Organizing the belt...")
belt.sort()
print(f"Sorted belt: {belt}")

if belt:
    print("A monster appears! Using first item in the belt...")
    used_item = belt.pop(0)
    print(f"Used {used_item}")

    health_points = random.randint(1, 6)
    if used_item in good_loot_options:
        health_points = min(6, health_points + 2)
        print(f"Health increased to {health_points}")
    elif used_item in bad_loot_options:
        health_points = max(0, health_points - 2)
        print(f"Health decreased to {health_points}")
    else:
        print("Item had no effect.")
else:
    print("No items in the belt!")


def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                         
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                  
      @              @                  
      """
    print(ascii_image)
    print(f"Player's weapon ({combat_strength}) ---> Monster ({m_health_points})")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("You have killed the monster")
    else:
        m_health_points -= combat_strength
        print(f"You have reduced the monster's health to {m_health_points}")
    return m_health_points


def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                           
      (     @*&@  ,                         
    @               %                       
     &#(@(@%@@@@@*   /                      
      @@@@@.                                
               @       /                    
                %         @                 
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)
    print(f"Monster's Claw ({m_combat_strength}) ---> Hero ({health_points})")
    if m_combat_strength >= health_points:
        health_points = 0
        print("You have been defeated!")
    else:
        health_points -= m_combat_strength
        print(f"The monster has reduced your health to {health_points}")
    return health_points


diceOptions = list(range(1, 7))
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

print("You meet the monster. FIGHT!!")
while m_combat_strength > 0 and health_points > 0:
    input("You strike first (Press Enter)")
    m_combat_strength = hero_attacks(m_combat_strength, health_points)
    if m_combat_strength == 0:
        print("Hero wins!")
    else:
        input("The monster strikes (Press Enter)")
        health_points = monster_attacks(m_combat_strength, health_points)
        if health_points == 0:
            print("Monster wins!")
