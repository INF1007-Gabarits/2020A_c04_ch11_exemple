import random


class LongSword:
    def __init__(self):
        self.damage = 20
        self.breaking_prob = 0.15
        self.resistance = 35
        self.is_broken = False

    def get_is_broken(self, damage_taken: int):
        if damage_taken > self.resistance and 0 <= random.random() < self.breaking_prob:
            self.is_broken = True

        return self.is_broken