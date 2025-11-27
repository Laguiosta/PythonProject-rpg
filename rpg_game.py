# Imports
import random
import os
import time

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

# Player variable
information_player = {
    "life": 500,
    "damage": 50,
    "block": random.randint(25, 30),
    "class": "",
    "inventory": ["health_potion"],
    "gold": 100,
    "mana": 50
}

player_stats = {
    "strength": 1,
    "intelligence": 1,
    "dexterity": 1
}

# Enemy variable
rats = {
    "monster": "Giant Rat",
    "life": 250,
    "damage": 35,
    "block": random.randint(15,20),
    "gold": 25
}


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
        combat_menu(rats)
        up_stats()
        print(information_player['damage'])

    else:
        print("Have a good day.")


# History Function

def game_history(history):
    def skip_history_function():
        skip_history = False
        while skip_history != True:
            user_choice_skip = input("Press Enter to continue ")
            if user_choice_skip == "":
                skip_history = True

    history1 = (
        "\nAn adventurer left the house he inherited from his missing father, "
        "leaving his mother to take care of it as he set out to explore the world.\n"
    )

    mother_history = '''
Mother:
“So… the day has finally come for you to leave.”
She tries to smile, but her eyes reveal the fear of someone who has already lost someone once.

You:
“I have to find out what happened to Dad. And I want to see the world outside.”

Mother:
“Your father said the exact same thing…”
'''

    tutorial_combat = '''
As soon as he left home and followed the old trail, the young adventurer heard quick scratches nearby. 
From behind broken crates, giant rats appeared, hissing and ready to attack.

It wasn’t a great danger — just a first test. The journey had truly begun.
'''

    history2 = "\nSun, the darkness takes me. I believe in you; one day, you will follow my path — the volc...\n"
    history3 = "\nThe father returned to normal, the world’s corruption vanished, and the young explorer returned home.\n"

    if history == 1:
        os.system("cls")
        print(history1)
        skip_history_function()
    elif history == 1.1:
        os.system("cls")
        print(mother_history)
        skip_history_function()
    elif history == 1.2:
        os.system("cls")
        print(tutorial_combat)
        skip_history_function()
    elif history == 2:
        os.system("cls")
        print(history2)
        skip_history_function()
    elif history == 3:
        os.system("cls")
        print(history3)
        skip_history_function()
    else:
        print("Error! Verify history variables.")


# Class and Stats System

def select_class():
    os.system("cls")
    print("\n1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    user_choice_class = int(input("Enter your class [1/2/3]: "))
    if user_choice_class == 1:
        print("\nYou picked Warrior")
        information_player["class"] = "warrior"
        player_stats["strength"] += 1
    elif user_choice_class == 2:
        print("\nYou picked Mage")
        information_player["class"] = "mage"
        player_stats["intelligence"] += 1
        information_player["mana"] += 100
        information_player["inventory"].append("mana_potion")
        mana_up()
    elif user_choice_class == 3:
        print("\nYou picked Rogue")
        information_player["class"] = "rogue"
        player_stats["dexterity"] += 1
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
             player_stats['strength'] += 1
             points -= 1
        elif choice_user == 2:
            player_stats['intelligence'] += 1
            points -= 1
        elif choice_user == 3:
            player_stats["dexterity"] += 1
            points -= 1
            class_damage_up()

def show_stats():
    print(f"""

    Stength: {player_stats['strength']}
    Intelligence: {player_stats['intelligence']}
    Dexterity: {player_stats['dexterity']}

""")




def class_damage_up():
    if information_player["class"] == "warrior":
        information_player["damage"] += player_stats["strength"] * 10
    elif information_player["class"] == "mage":
        information_player["damage"] += player_stats["intelligence"] * 10
    elif information_player["class"] == "rogue":
        information_player["damage"] += player_stats["dexterity"] * 10


def mana_up():
    information_player["mana"] += player_stats["intelligence"] * 10


def block_damage(enemy):
    print("You tried to defend.")
    if enemy["damage"] > information_player["block"]:
        damage_taken = enemy["damage"] - information_player["block"]
        print("You failed to defend.")
        print(f"Damage taken: {damage_taken}")
        information_player['life'] - damage_taken
    else:
        print("You successfully defended!")
    time.sleep(1)

def combat_menu(enemy): 
    while enemy["life"] > 0 and information_player['life'] > 0:
        os.system("cls")
        print(f"""
  ==========================
          BATTLE MENU
  ==========================
  Enemy: {enemy['monster']}   HP: {enemy['life']}
  You:   Adventurer           HP: {information_player['life']}  MP: {information_player['mana']}

  1) Attack
  2) Skill
  3) Defend
  4) Item
  ==========================
  Enter choice [1-4]:""")

        user_choice = int(input(""))

        if user_choice == 1:
            enemy_taken_damage = information_player['damage'] - enemy['block']
            os.system('cls')

            print(f"You dealt {enemy_taken_damage} damage")
            enemy['life'] -= enemy_taken_damage
            if enemy['life'] <= 0:
                print('You killed him')
                time.sleep(1.5)
                break
            #   Enemy turn
            player_taken_damage = enemy['damage'] - information_player['block']  
            information_player['life'] -= player_taken_damage
            os.system('cls')

            print(f"""
  ==========================
          ENEMY TURN
  ==========================

    {enemy['monster']} will attatck!
    He dealt {player_taken_damage}!
""")
            time.sleep(2)


start_game()