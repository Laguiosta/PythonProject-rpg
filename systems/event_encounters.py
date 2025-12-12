import random
import sys
from systems.combat_system import combat
from entities.enemies import *
from entities.player import *
from systems.dialogue_system import game_history
import time
import os

# Function called event encounter
# Dialogue camping
# Recive class with parameters 

def skip_history_function():
    skip_history = False
    while skip_history != True:
        user_choice_skip = input("\nPress Enter to continue ")
        if user_choice_skip == "":
            skip_history = True

def skip_camping_rest():
    while True:
        user_choice = input("Do u want rest? (yes/no)").strip().lower()
        if user_choice in ('yes', 'y'):
            player.life = 500
            print(f'Resting', end='', flush=True)
            for i in range(3):
                time.sleep(0.5)
                print('.', end='', flush=True)
            break
        elif user_choice in ('no', 'n'):
            print(f'Loading', end='', flush=True)
            for i in range(3):
                time.sleep(0.5)
                print('.', end='', flush=True)
            break
        else:
            print('\nTry Again')


def camping_event(job):
    dice = random.randint(1, 3)

    # EVENT 1 ================================================
    if dice == 1:
        os.system('cls')
        print("\nExhaustion weighs heavily on you; the road ahead will have to wait. You decide to make camp here and rest for the night.")
        time.sleep(1)

        if job == "warrior":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nAs you slept, you sensed the atmosphere shift. Jolting awake, you rose to investigate and spotted two bandits planning an attack on you. Without hesitation, you struck first gaining the advantage.")
                skip_history_function()
                bandits.life = 400
                combat(bandits, player)
                skip_camping_rest()
            else:
                print("\nWhile you slept, nothing seemed out of place — until two bandits suddenly ambushed you, giving you no time to react")
                skip_history_function()
                combat(bandits, player)
                skip_camping_rest()

        elif job == "mage":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nAs you slept, the arcane offered no warning. Then, in an instant, two bandits burst from the shadows, catching the mage off guard before any spell could be cast.")
                skip_history_function()
                bandits.life = 400
                combat(bandits, player)
                skip_camping_rest()
            else:
                print("\nIn your slumber, the arcane remained silent offering no hint of danger. Then, without warning, two bandits struck, catching the mage completely off guard.")
                skip_history_function()
                combat(bandits, player)
                skip_camping_rest()

        elif job == "rogue":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nEven in sleep, a rogue's instincts never rest. Feeling the subtle shift in the air, you woke without a sound. Seeing two bandits preparing an ambush, you moved first, striking from the shadows before they could act.")
                skip_history_function()
                bandits.life = 400
                combat(bandits, player)
                skip_camping_rest()
            else:
                print("\nFor once, even a rogue’s instincts proved silent. In the stillness of sleep, no hint of danger reached you — until two bandits struck out of nowhere, catching you completely off guard.")
                skip_history_function()
                combat(bandits, player)
                skip_camping_rest()

    # EVENT 2 ================================================
    elif dice == 2:
        os.system('cls')
        print("\nWeariness settles deep into your bones; the journey must wait. You set up camp and allow yourself a moment of rest.")
        time.sleep(1)

        if job == "warrior":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nA warrior never sleeps completely defenseless. A faint crunch of leaves snapped you awake — goblins creeping toward your campfire. You rose before they even realized you'd noticed them, taking the first move.")
                skip_history_function()
                goblins.life = 700
                combat(goblins, player)
                skip_camping_rest()
            else:
                print("\nYour body gave in to exhaustion, and sleep came too deep. When you finally stirred, shrill goblin cries filled the air — they were already on top of you, leaving no time to prepare.")
                skip_history_function()
                combat(goblins, player)
                skip_camping_rest()

        elif job == "mage":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nA ripple in the arcane disturbed your dreams. Eyes snapping open, you sensed goblin shapes skulking around your camp. With a quick incantation, you unleashed the first strike before they knew you were awake.")
                skip_history_function()
                goblins.life = 700
                combat(goblins, player)
                skip_camping_rest()
            else:
                print("\nThe magic offered no warning tonight. You woke only when a goblin’s blade scraped against stone nearby — and by then, their ambush had already begun.")
                skip_history_function()
                combat(goblins, player)
                skip_camping_rest()

        elif job == "rogue":
            dice = random.randint(1, 2)
            if dice == 1:
                print("\nEven asleep, a rogue's senses remain razor-sharp. A shift in the darkness made you open your eyes silently. Spotting goblins crawling into position, you slipped into the shadows and struck before they noticed your escape.")
                skip_history_function()
                goblins.life = 700
                combat(goblins, player)
                skip_camping_rest()
            else:
                print("\nTonight, even your instincts faltered. You slept soundly — too soundly. By the time your eyes opened, goblins were already lunging from every direction.")
                skip_history_function()
                combat(goblins, player)
                skip_camping_rest()

    # EVENT 3 — DRAGON =======================================
    elif dice == 3:
        os.system('cls')
        print("\nThe night is calm as you settle down to rest... until a thunderous roar shakes the sky above.")
        time.sleep(1)
        print("A massive dragon cuts through the clouds, its wings beating like storms. Its scales glow like molten stone.\n")
        time.sleep(1)

        print("What will you do?")
        print("1) Look up at the dragon")
        print("2) Hide immediately\n")

        choice = int(input("Enter choice [1-2]: "))

        # PLAYER LOOKS AT DRAGON =====================================
        if choice == 1:
            print("\nYou stare up in awe, frozen by the sight of the majestic beast...")
            time.sleep(1)
            print("The dragon's head snaps toward you, its eyes burning with fury.")
            time.sleep(1)

            # 50% CHANCE: GAIN SKILL OR DIE
            dice = random.randint(1, 2)

            if dice == 1:
                print("\nInstead of firing, the dragon releases a burst of raw energy that washes over you.")
                time.sleep(1)
                print("Your body trembles as you absorb a fraction of its ancient power!")
                print("You learned a new skill: +1 Strength!")
                player.add_stat("strength", 1)
                skip_camping_rest()
            else:
                print("\nThe dragon inhales sharply...")
                time.sleep(1)
                print("A massive fireball erupts from its jaws, engulfing everything around you!")
                time.sleep(1.3)
                print("\nYou were incinerated instantly.")
                player.life = 0
                sys.exit(0)

        # PLAYER HIDES ==============================================
        elif choice == 2:
            print("\nYou immediately dive behind a fallen tree, heart pounding.")
            time.sleep(1)
            print("The dragon passes overhead, unaware of your presence...")
            time.sleep(1.2)
            print("\nYou survive, but gain nothing.")
            skip_camping_rest()


def merchant_event():
    game_history(1.3)
