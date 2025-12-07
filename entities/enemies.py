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