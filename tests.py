class Npc:
    def __init__(self, name, life, damage, mana):
        self.name = name
        self.life = life
        self.damage = damage
        self.mana = mana
        self.items = {
            'Health Potion': {
                'quanty': 3,
                'price': 50
            },

            'Iron Dagger': {
                'quanty': 1,
                'price': 150,
            },
            'iron Sword':{
                'quanty': 1,
                'price': 150,
            },
            'Old staff': {
                'quanty': 1,
                'price': 150
            },
            'Mana Potion':{
                'quanty': 2,
                'price': 50
            }
        }

jimmy_bob = Npc(
    name = 'Jimmy Bob',
    life = 1000,
    damage = 500,
    mana = 300,

)
