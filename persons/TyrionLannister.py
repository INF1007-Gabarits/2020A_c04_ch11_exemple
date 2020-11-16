from HighBorn import HighBorn
from Axe import Axe
import random


class TyrionLannister:
    def __init__(self):
        self.name = "Tyrion Lannister"
        self.title = HighBorn()
        self.sex = "M"
        self.weapon = Axe()
        self.strength = 5
        self.accuracy = 0.60
        self.paring_prob = 0.50
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
