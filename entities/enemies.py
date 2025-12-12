class Enemy:
    def __init__(self, monster, life, damage, mana):
        self.monster = monster
        self.life = life
        self.damage = damage
        self.mana = mana

rats = Enemy(
    monster = 'Rats',
    life = 200,
    damage = 50,
    mana = 25
)

bandits = Enemy(
    monster = 'Bandit',
    life = 500,
    damage = 85,
    mana = 50
)

wolves = Enemy(
    monster = 'Wolves',
    life = 1000,
    damage = 100,
    mana = 200
)

goblins = Enemy(
    monster = 'Goblins',
    life = 1300,
    damage = 150,
    mana = 100
)

father = Enemy(
    monster = 'Corrupted Father',
    life = 3000,
    damage = 200,
    mana = 500
)