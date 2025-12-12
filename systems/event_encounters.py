import random
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


def camping_event(job):
    os.system('cls')
    print("\nExhaustion weighs heavily on you; the road ahead will have to wait. You decide to make camp here and rest for the night.")
    time.sleep(1)
    if job == "warrior":
        dice = random.randint(1, 2) # 1 = Advantage, 2 = normal battle
        if dice == 1:
            print("\nAs you slept, you sensed the atmosphere shift. Jolting awake, you rose to investigate and spotted two bandits planning an attack on you. Without hesitation, you struck first gaining the advantage.")
            skip_history_function()
            bandits.life = 400
            combat(bandits, player)
        else:
            print("\nWhile you slept, nothing seemed out of place — until two bandits suddenly ambushed you, giving you no time to react")
            skip_history_function()
            combat(bandits, player)
    elif job == "mage":
        dice = random.randint(1, 2)
        if dice == 1:
            print("\nAs you slept, the arcane offered no warning. Then, in an instant, two bandits burst from the shadows, catching the mage off guard before any spell could be cast.")
            skip_history_function()
            bandits.life = 400
            combat(bandits, player)
        else:
            print("\nIn your slumber, the arcane remained silent offering no hint of danger. Then, without warning, two bandits struck, catching the mage completely off guard.")
            skip_history_function()
            combat(bandits, player)
    elif job == "rogue":
        dice = random.randint(1, 2)
        if dice == 1:
            print("\nEven in sleep, a rogue's instincts never rest. Feeling the subtle shift in the air, you woke without a sound. Seeing two bandits preparing an ambush, you moved first, striking from the shadows before they could act.")
            skip_history_function()
            bandits.life = 400
            combat(bandits, player)
        else:
            print("\nFor once, even a rogue’s instincts proved silent. In the stillness of sleep, no hint of danger reached you — until two bandits struck out of nowhere, catching you completely off guard.")
            combat(bandits, player)

def merchant_event():
    game_history(1.3)