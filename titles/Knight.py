class Knight:
    def __init__(self):
        self.is_predictable = False
        self.is_rich = True
        self.calling = "Sir"

    def get_calling(self, person) -> str:
        return self.calling

    def __lt__(self, other):
        return not self.is_predictable

    def __eq__(self, other):
        if self.is_predictable == other.is_predictable:
            return True
