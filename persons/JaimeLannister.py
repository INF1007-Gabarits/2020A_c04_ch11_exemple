from Knight import Knight
from ShortSword import ShortSword
import random


class JaimeLannister:
    def __init__(self):
        self.name = "Jaime Lannister"
        self.title = Knight()
        self.sex = "M"
        self.weapon = ShortSword()
        self.strength = 30
        self.accuracy = 0.95
        self.paring_prob = 0.90
        self.health = 100

    def is_attack_success(self):
        if 0 <= random.random() < self.accuracy:
            return True

        return False

    def is_paring_success(self):
        if 0 <= random.random() < self.paring_prob:
            return True

        return False

    def get_total_damage(self):
        return self.strength + self.weapon.damage
