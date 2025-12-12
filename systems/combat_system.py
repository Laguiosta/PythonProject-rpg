import os
import time

from entities.enemies import *    
from entities.player import player, Player


def combat(enemy, player) -> None: 
    while enemy.life > 0 and player.life > 0:
        os.system("cls")
        print(f"""
  ==========================
          BATTLE MENU
  ==========================
  Enemy: {enemy.monster}   HP: {enemy.life}
  You:   Adventurer        HP: {player.life}  MP: {player.mana}

  1) Attack
  2) Skill
  3) Defend
  4) Item
  ==========================
  Enter choice [1-4]:""")

        user_choice = int(input(""))

        # ATTACK
        if user_choice == 1:
            os.system('cls')

            print(f"You dealt {player.damage} damage")
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

        # ITEM MENU
        if user_choice == 4:
            os.system("cls")
            print("=== YOUR ITEMS ===")
            if not player.player_inventory:
                print("You have no items!")
                time.sleep(1.5)
                continue

            for i, (item, q) in enumerate(player.player_inventory.items(), 1):
                print(f"{i}) {item} x{q}")

            choice = int(input("\nChoose item number: ")) - 1

            item_list = list(player.player_inventory.keys())

            if 0 <= choice < len(item_list):
                item_chosen = item_list[choice]
                used = player.use_item(item_chosen)

                if used:
                    time.sleep(1.5)

                    # Enemy counter-attack
                    player.life -= enemy.damage
                    print(f"\nEnemy attacked for {enemy.damage}!")
                    time.sleep(1.5)
            else:
                print("Invalid choice!")
                time.sleep(1)
                continue
