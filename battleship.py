import random


class BattleShip:

    def __init__(
            self,
            length,
            direction,
    ):
        self.length = length
        self.direction = direction

    def place_ship(
            self,
            field,
            max_field,
    ):
        min_field = 1
        field = field
        x = random.choice(range(min_field, max_field))
        y = random.choice(range(min_field, max_field))

        return [x, y, field]

    def __str__(self):
        return '{}, {}'.format(self.length, self.direction)

    @classmethod
    def place_submarine(cls):
        return cls(length=10, direction='vertical')

    @classmethod
    def place_destroyer(cls):
        return cls(length=10, direction='vertical')

    @classmethod
    def place_cruiser(cls):
        return cls(length=10, direction='vertical')

    @classmethod
    def place_carrier(cls):
        return cls(length=10, direction='vertical')