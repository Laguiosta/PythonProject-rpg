information_player = {
    "life": 500,
    "damage": 50,
    "block": 35,
    "class": "",
    "inventory": ['health_potion'],
    "gold": 100,
    "mana": 50
} 

rats = {
    "life": 250,
    "damage": 35,
    "block": 0,
    "gold": 25
}


def combat_menu():
  while(rats["life"]):
    print(f"""
  ==========================
        BATTLE MENU
  ==========================
  Enemy: Giant Rat        HP: {rats['life']}
  You:   Adventurer       HP: {information_player['life']}  MP: {information_player['mana']}

  1) Attack
  2) Skill
  3) Defend
  4) Item
  5) Status
  6) Flee
  ==========================
  Enter choice [1-6]:
  """)
    user_choice = int(input(''))
    if user_choice == 1:
      print(f"You dealt {information_player['damage']} damage!")
      rats['life'] -= information_player['damage']
      print(f"Enemy remeaning HP: {rats['life']}")
    stop = int(input("Stop"))

    
combat_menu()