from Bastard import Bastard
from LongSword import LongSword
import random


class JohnSnow:
    def __init__(self):
        self.name = "John Snow"
        self.title = Bastard()
        self.sex = "M"
        self.weapon = LongSword()
        self.strength = 40
        self.accuracy = 0.80
        self.paring_prob = 0.85
        self.health = 200

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
