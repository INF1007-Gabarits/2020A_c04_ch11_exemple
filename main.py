from AryaStark import AryaStark
from JaimeLannister import JaimeLannister
from JohnSnow import JohnSnow
from TyrionLannister import TyrionLannister
from Fight import Fight


def select_fighter(fighters: list):
    while True:
        name = input("Please enter a fighter name\n")
        for fighter in fighters:
            if name.lower() in fighter.name.lower():
                return fighter

        print("This fighter does not exist")


if __name__ == "__main__":
    fighters = [AryaStark(), JohnSnow(), TyrionLannister(), JaimeLannister()]
    fighter1 = select_fighter(fighters)
    fighter2 = select_fighter(fighters)

    fight = Fight(fighter1, fighter2)
    fight.start()
