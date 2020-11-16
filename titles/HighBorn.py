class HighBorn:
    def __init__(self):
        self.is_predictable = True
        self.is_rich = True

    def get_calling(self, person) -> str:
        if person.sex == "M":
            return "My lord"

        return "My lady"

    def __lt__(self, other):
        return not self.is_predictable

    def __eq__(self, other):
        if self.is_predictable == other.is_predictable:
            return True
