import random


class Hammer:
    def __init__(self):
        self.damage = 20
        self.__breaking_prob = 0.1
        self.__resistance = 40
        self.__is_broken = False

    def get_is_broken(self, damage_taken: int):
        if damage_taken > self.__resistance and 0 <= random.random() < self.__breaking_prob:
            self.__is_broken = True

        return self.__is_broken



