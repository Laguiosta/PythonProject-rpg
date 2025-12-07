class Player:
    def __init__(self, life, damage, mana, job): # Job is class
        self.life = life
        self.damage = damage
        self.mana = mana
        self.job = job
        self.player_stats = {
            "strength": 1,
            "intelligence": 1,
            "dexterity": 1
    }

        
    def add_stat(self, stat, value):
        self.player_stats[stat] += value

#   Player variable
player = Player(
    life = 500,
    damage = 50,
    mana = 0,
    job = '',


)