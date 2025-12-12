from entities.player import player   # import the already created player object

class Npc:
    def __init__(self, name, life, damage, mana):
        self.name = name
        self.life = life
        self.damage = damage
        self.mana = mana
        self.items = {
            'Health Potion':  {'quanty': 3, 'price': 50},
            'Iron Dagger':    {'quanty': 1, 'price': 150},
            'Iron Sword':     {'quanty': 1, 'price': 150},
            'Old Staff':      {'quanty': 1, 'price': 150},
            'Mana Potion':    {'quanty': 2, 'price': 50},
        }

    def showItems(self):
        text = "\n===== NPC SHOP INVENTORY =====\n"
        for item_name, data in self.items.items():
            quanty = data['quanty']
            price = data['price']
            text += f'{item_name:<15} | R${price:<3} | qty:{quanty:<5}\n'
        text += "================================\n"
        return text
    

    def buyItems(self):
        while True:

            # Show NPC inventory each loop
            print(self.showItems())

            user_choice = input("Enter your item: ")

            # Item doesn't exist
            if user_choice not in self.items:
                print("\nSorry pal, but I don't have this item. Pick another.\n")
                continue

            # Add item to player's inventory (creates or increases quantity)
            player.add_item_inventory(user_choice, 1)

            # Reduce quantity from NPC's stock
            self.items[user_choice]['quanty'] -= 1

            # Remove item from NPC if quantity is zero
            if self.items[user_choice]['quanty'] == 0:
                del self.items[user_choice]

            print(f"\nYou bought 1x {user_choice}!")

            # Ask if player wants to buy again
            again = input("\nDo you want to buy something else? (yes/no): ").strip().lower()

            if again not in ("yes", "y"):
                print("\nThanks for buying! Come back anytime.")
                break


# NPC instance
jimmy_bob = Npc(
    name='Jimmy Bob',
    life=1000,
    damage=500,
    mana=300,
)
