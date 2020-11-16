import random


class Fist:
    def __init__(self):
        self.damage = 0
        self.is_broken = False

    def get_is_broken(self, damage_taken: int):

        return self.is_broken