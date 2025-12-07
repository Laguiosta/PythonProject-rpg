# Imports
import random
import os
from entities.player import *
from entities.enemies import *
from systems.dialogue_system import game_history
from systems.combat_system import combat

"""
Principal: Start, Middle, End

Rule History: A man. The world is a classic RPG.

History:
    1. An adventurer left the house he inherited from his missing father,
       leaving his mother to take care of it as he set out to explore the world.
    2. Sun, the darkness takes me. I believe in you; one day, you will follow my path — the volc...
    3.1 The father appears, but it isn’t him — the darkness has taken him.
    Extra: Happy ending.

Systems:
    Chance: We’ll have a chance-based impact system with items
            (successfully: escape, defense — passives: block, dodge).
    Chance-Encounters: Mini-encounters resolved based on stats.
    Difficulty System:
        Easy: 90%  |  Medium: 75%  |  Hard: 50%
        (The world has a difficulty level, and NPCs, battles, and skills interact with it.)

Start:
    1. Story 1
    2. Predefined character.
    3. Classes = Mage, Warrior, Rogue (each class has its own advantages).
----------------------------------------------------------------------------
    1.1 Initial Items – each class has exclusive starting items.
    1.2 Initial Stats – each class has predefined starting stats.
    1.3 Difficulty – Easy, Medium, Hard.
----------------------------------------------------------------------------
    2.1 Talk to mother – Luck test
    2.2 First combat with rats
    2.3 Camping
----------------------------------------------------------------------------

Middle:
    1. After camping, perform Tests (Luck, Intelligence, Strength)
            1.1 Luck – After sleeping, find an item. Failed = battle
            1.2 Intelligence – Wake early and avoid bandits. Failed = battle
            1.3 Strength – Start a battle with advantage. Failed = battle
    2. Two routes
            Route 1 = NPC Encounter – test (Strength: help NPC, Luck: steal) – Failed = battle
            Route 2 = NPC Encounter – test (Intelligence: help NPC, Game-chance) – Failed = battle
    3. Merchant encounter
            Luck (steal) = gain gold – Failed = battle
            Intelligence = new skill – Failed = nothing
            Game-chance = better price
            Buy items
----------------------------------------------------------------------------

End:
    1. Combat (Wolves)
    2. Camping (system)
    3. Two routes (Routes system)
-------------------------------------------------------------------------------
    1.1 Merchant (system)
    1.2 Clue about father
    1.3 Story 2
--------------------------------------------------------------------------------
    2.1 Enter volcano (battle)
    2.2 Middle of volcano (rest)
    2.3 Battle with father
    Extra: Story 3
"""

# Temporary dev-tasks

# Start_game    (x)
# Difficulty    (x)
# History       (x)
# Select class  (x)
# Initial items (x)
# Initial stats (x)
# Stats structure = what I need to add: 
# damage based on stats (x), mana based on intelligence (x)

# World variable
world_difficulty = str()



# Enemy variable



def start_game():
    print("1. Start Game")
    print("2. Exit")
    user_choice = int(input("Select your choice [1/2]: "))
    os.system("cls")

    if user_choice == 1:
        def select_difficulty():
            print("1. Easy")
            print("2. Medium")
            print("3. Hard")
            global world_difficulty
            user_choice_difficulty = int(input("Enter your difficulty [1/2/3]: "))
            if user_choice_difficulty == 1:
                world_difficulty = "Easy"
            elif user_choice_difficulty == 2:
                world_difficulty = "Medium"
            elif user_choice_difficulty == 3:
                world_difficulty = "Hard"

        select_difficulty()
        os.system("cls")
        game_history(1)
        select_class()
        game_history(1.1)
        game_history(1.2)
        combat(rats, player)
        up_stats()
        print(player.damage)

    else:
        print("Have a good day.")






# Class and Stats System

def select_class():
    os.system("cls")
    print("\n1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    user_choice_class = int(input("Enter your class [1/2/3]: "))
    if user_choice_class == 1:
        print("\nYou picked Warrior")
        player.job = 'warrior'
        player.mana = 50
        player.add_stat('strength', 1)
    elif user_choice_class == 2:
        print("\nYou picked Mage")
        player.job = 'mage'
        player.mana = 200
        player.add_stat("intelligence", 1)
        mana_up()
    elif user_choice_class == 3:
        print("\nYou picked Rogue")
        player.job = 'rogue'
        player.mana = 125
        player.add_stat("dexterity", 1)
    else:
        print("Error!")

    class_damage_up()

def up_stats():
    points = 3
    while points > 0:
        os.system('cls')
        print(f"""
    ==========================
            LEVEL UP!
    ==========================
        You have {points} points!

        Wich stas do you want up
            
        1.  Strength
        2.  Intelligence
        3.  Dexterity  
    """)
        choice_user = int(input(""))
        if choice_user == 1:
             player.add_stat('strength', 1)
             points -= 1
        elif choice_user == 2:
            player.add_stat('intelligence', 1)
            points -= 1
        elif choice_user == 3:
            player.add_stat("dexterity", 1)
            points -= 1
            class_damage_up()

def show_stats():
    print(f"""

    Stength: {player.player_stats['strength']}
    Intelligence: {player.player_stats['intelligence']}
    Dexterity: {player.player_stats['dexterity']}

""")




def class_damage_up():
    if player.job == "warrior":
        player.damage += player.player_stats["strength"] * 10
    elif player.job == "mage":
        player.damage += player.player_stats["intelligence"] * 10
    elif player.job == "rogue":
        player.damage += player.player_stats["dexterity"] * 10


def mana_up():
    player.mana += player.player_stats["intelligence"] * 10





start_game()