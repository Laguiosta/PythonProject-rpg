import os
import time
from entities.enemies import *
from entities.player import *

def combat(enemy, player) -> None: 
    while enemy.life > 0 and player.life > 0:
        os.system("cls")
        print(f"""
  ==========================
          BATTLE MENU
  ==========================
  Enemy: {enemy.monster}   HP: {enemy.life}
  You:   Adventurer           HP: {player.life}  MP: {player.mana}

  1) Attack
  2) Skill
  3) Defend
  4) Item
  ==========================
  Enter choice [1-4]:""")

        user_choice = int(input(""))

        if user_choice == 1:
            os.system('cls')

            print(f"You dealt {player.damage } damage")
            time.sleep(0.5)
            enemy.life -= player.damage 

            if enemy.life <= 0:
                print('You killed him')
                time.sleep(1.5)
                break

            # Enemy turn
            player.life -= enemy.damage
            os.system('cls')

            print(f"""
  ==========================
          ENEMY TURN
  ==========================

    {enemy.monster} will attack!
    He dealt {enemy.damage}!
""")
            time.sleep(2)
