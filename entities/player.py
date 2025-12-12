class Player:
    def __init__(self, life, damage, mana, job):  # job = character class
        self.life = life
        self.damage = damage
        self.mana = mana
        self.job = job
        # Base stats for the player
        self.player_stats = {
            "strength": 1,
            "intelligence": 1,
            "dexterity": 1
        }

        # Player inventory (item_name: quantity)
        self.player_inventory = {
            'Health Potion': 2
        }

    def add_stat(self, stat, value):
        # Increase a specific stat by a given value
        self.player_stats[stat] += value

    def show_inventory(self):
        # Display all items and their quantities
        for item, quanty in self.player_inventory.items():
            print(f"{item}: {quanty}")

    def add_item_inventory(self, item, quanty):
        # Adds an item to the inventory or increases its quantity
        self.player_inventory[item] = self.player_inventory.get(item, 0) + quanty

    # ================================
    #       ITEM SYSTEM
    # ================================
    def use_item(self, item_name):
        """Uses an item and triggers its effect."""

        if item_name not in self.player_inventory:
            print("You don't have this item!")
            return False

        if self.player_inventory[item_name] <= 0:
            print("You're out of this item!")
            return False

        # Map item names to effect functions
        item_effects = {
            "Health Potion": self.use_health_potion,
            "Mana Potion": self.use_mana_potion
        }

        if item_name not in item_effects:
            print("This item cannot be used!")
            return False

        # Execute the effect
        item_effects[item_name]()

        # Subtract 1 from inventory
        self.player_inventory[item_name] -= 1

        if self.player_inventory[item_name] == 0:
            del self.player_inventory[item_name]

        return True

    # ITEM EFFECTS ------------------

    def use_health_potion(self):
        heal = 300
        self.life += heal
        print(f"You used a Health Potion and recovered {heal} HP!")

    def use_mana_potion(self):
        regen = 30
        self.mana += regen
        print(f"You used a Mana Potion and recovered {regen} MP!")



# Player instance (global player object)
player = Player(
    life=500,
    damage=50,
    mana=0,
    job='',
)
