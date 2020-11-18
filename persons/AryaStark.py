from HighBorn import HighBorn
from Needle import Needle
import random


class AryaStark:
    def __init__(self):
        self.__name = "Arya Stark"
        self.title = HighBorn()
        self.__sex = "F"
        self.weapon = Needle()
        self.strength = 10
        self.accuracy = 0.99
        self.paring_prob = 0.95
        self.health = 100

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

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

