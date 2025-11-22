# Imports
import random
import os


"""
Principal: Start, Middle, End


Rule History: A man. The world is a classic RPG.

History:
    1. An adventurer left the house he inherited from his missing father, leaving his mother to take care of it as he set out to explore the world.
    2. Sun, the darkness takes me. I believe in you; one day, you will follow my path — the vulc...
    3.1 The father appears, but it isn’t him — the darkness has taken him.
    Extra: Happy ending.


Systems:
    Chance: We'll have a chance-based impact system with items (successfully: escape, defense — passives: block, dodge).
    Chance-Encounters: Basically mini-encounters resolved based on status.
    Difficulty System:
        Easy: 90%  |  Medium: 75%  |  Hard: 50%
        (Basically, the world has a difficulty level, and each NPC, battle, and skill interacts with this world difficulty.)

Start:
    1.  Story 1
    2.  Predefined character.
    3.  Classes = Mage, Warrior, and Rogue (each class has its own advantages).
----------------------------------------------------------------------------
    1.1 Initial Items – (each class has exclusive starting items).
    1.2 Initial Status – (each class has predefined starting stats).
    1.3 Difficulty – Easy, Normal, Hard.
----------------------------------------------------------------------------
    2.1 Talk to mother – Luck test
    2.2 First combat with rats
    2.3 Camping
----------------------------------------------------------------------------

Middle:
    1.  After camping, perform Tests (Luck, Intelligence, Strength)
            1.1 Luck – After sleeping, find an item. Failed = battle
            1.2 Intelligence – Wake up early to avoid bandits. Failed = battle
            1.3 Strength – Start a battle with advantage. Failed = battle
    2.  Two routes
            Route 1 = NPC Encounter – test(Strength: help NPC, Luck: steal) – Failed = battle
            Route 2 = NPC Encounter – test(Intelligence: help NPC, Game-chance) – Failed = battle
    3.  Merchant encounter
            Luck (steal) = gain gold – Failed = battle
            Intelligence = new skill – Failed = nothing
            Game-chance = better price
            Buy items
----------------------------------------------------------------------------

End:
    1.  Combat (Wolves)
    2.  Camping (Camping system)
    3.  Two routes (Routes system)
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

#   Temporary dev-tasks

#   Start_game    (x)
#   Difficulty    (x)
#   History       (x)
#   Select class  (x)
#   Initial items (x)
#   Initial stats (x)
#   Stats structure = what I need to add: damage based on status (x), block based on strength ( ), mana based on intelligence ( ), pickpocket based on dexterity ( ), dodge based on dexterity ( )

# Variable World
world_difficulty = str()

# Variable player
information_player = {
    "life": 500,
    "damage": 50,
    "block": 35,
    "class": "",
    "inventory": ['health_potion'],
    "gold": 100
} 

player_stats = {
    "strength": 1,
    "intelligence": 1,
    "dexterity": 1,
}

def start_game():
    print("1.   Start Game")
    print("2.   Exit")
    user_choice = int(input("Select your choice[1/2]: "))
    os.system("cls")
    if user_choice == 1:
        def select_difficulty():
            print("1.   Easy")
            print("2.   Medium")
            print("3.   Hard")
            global world_difficulty
            user_choice_difficulty = int(input("Enter your difficulty[1/2/3]: "))
            if user_choice_difficulty == 1:
                world_difficulty = 'Easy'
            elif user_choice_difficulty == 2:
                world_difficulty = 'Medium'
            elif user_choice_difficulty == 3:
                world_difficulty = 'Hard'

        select_difficulty()
        os.system('cls')
        game_history(1)
        select_class()
    else:
        print("Have a good day")

#   Functions History

def game_history(history):
    def skip_history_function():
        skip_history = False
        while skip_history != True:
            user_choice_skip = input("Press enter to skip ")
            if user_choice_skip == "":
                skip_history = True

    history1 = "\nAn adventurer left the house he inherited from his missing father, leaving his mother to take care of it as he set out to explore the world.\n"
    history2 = "\nSun, the darkness takes me. I believe in you; one day, you will follow my path — the vulc...\n"
    history3 = "\nThe father returned to his normal self, the world’s corruption vanished, and the young explorer returned home alongside his father.\n"

    if history == 1:
        print(history1)
        skip_history_function()
    elif history == 2:
        print(history2)
        skip_history_function()
    elif history == 3:
        print(history3)
        skip_history_function()
    else:
        print("Error! Verify history variables")

#   Functions stats/class system

def select_class():
    os.system("cls")
    print("\n1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    user_choice_class = int(input("Enter your class[1/2/3]: "))
    if user_choice_class == 1:
        print(f"\nYou picked Warrior")
        information_player["class"] = "warrior"
        player_stats["strength"] += 1
    elif user_choice_class == 2:
        print(f"\nYou picked Mage")
        information_player["class"] = "mage"
        player_stats["intelligence"] += 1
        information_player["inventory"].append("mana_potion")
    elif user_choice_class == 3:
        print(f"\nYou picked Rogue")
        information_player["class"] = "rogue"
        player_stats["dexterity"] += 1
    else:
        print("Error!")

    class_damage_up()

def class_damage_up():
    if information_player["class"] == "warrior":
        information_player["damage"] += (player_stats["strength"] * 10)
    elif information_player["class"] == "mage":
        information_player["damage"] += (player_stats["intelligence"] * 10)
    elif information_player["class"] == "rogue":
        information_player["damage"] += (player_stats["dexterity"] * 10)

start_game()
