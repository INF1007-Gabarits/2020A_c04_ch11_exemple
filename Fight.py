from AryaStark import AryaStark
from JohnSnow import JohnSnow
from Fist import Fist
import random

class Fight:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def __first_fight(self):
        if self.fighter1.title == self.fighter2.title:
            fighter_list = [self.fighter1, self.fighter2]
            random.shuffle(fighter_list)

            return fighter_list[0], fighter_list[1]

        if self.fighter1.title < self.fighter2.title:
            return self.fighter2, self.fighter1

        return self.fighter1, self.fighter2

    def __salutation(self):
        fighters = [self.fighter1, self.fighter2]
        for index, fighter in enumerate(fighters):
            print(f"My name is {fighter.name}. I salute you {fighters[index - 1].title.get_calling(fighters[index - 1])}")

    def __round_phase(self, attacker, defender):
        print(f"{attacker.name} swings a {attacker.weapon.__class__.__name__}.")
        if attacker.is_attack_success():
            print(f"{attacker.name} hits {defender.name}!")
            self.__defense_phase(attacker, defender)

        else:
            print(f"{attacker.name} failed to attack {defender.name}!")

    def __defense_phase(self, attacker, defender):
        if defender.is_paring_success():
            print(f"{defender.name} successfully block {attacker.name}'s attack!")
            self.__weapon_survivership(attacker, defender)
        else:
            print(f"{defender.name} fails to block {attacker.name}'s attack!")
            print(f"{defender.name} takes {attacker.get_total_damage()}pts of damage...")
            defender.health -= attacker.get_total_damage()
            print(f"{defender.name} has only {defender.health} health points left...")

    def __weapon_survivership(self, attacker, defender):
        if defender.weapon.get_is_broken(attacker.get_total_damage()):
            print(f"Unfortunately {defender.name}'s {defender.weapon.__class__.__name__} is detroyed!!!")
            defender.weapon = Fist()

    def start(self):
        print("The fight begins")
        self.__salutation()

        attacker, defender = self.__first_fight()
        round_number = 1
        while self.fighter1.health > 0 or self.fighter2.health > 0:
            print(f"Round {round_number}")
            self.__round_phase(attacker, defender)
            attacker, defender = defender, attacker
            round_number += 1

        print(f"{attacker.name} is dead :(")







