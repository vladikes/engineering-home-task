import random


class BattleShip:

    def __init__(
            self,
            ship_length,
            direction,
            max_field_grid,
            field,
    ):
        self.ship_length = ship_length
        self.direction = direction
        self.max_field_grid = max_field_grid
        self.field = field
        self.place_ship()

    def place_ship(
            self,
    ):
        min_field_grid = 1
        x = random.choice(range(min_field_grid, self.max_field_grid,))
        y = random.choice(range(min_field_grid, self.max_field_grid,))

        return [
                x, y,
                self.field,
                self.ship_length,
                self.direction,
        ]

    def __str__(self):
        return '{}, {}'.format(self.ship_length, self.direction,)

    @classmethod
    def place_submarine(cls):
        return cls(
            ship_length=10,
            direction='vertical',
            field=None,
            max_field_grid=10,
        )

    @classmethod
    def place_destroyer(cls):
        return cls(
            ship_length=10,
        )

    @classmethod
    def place_cruiser(cls):
        return cls(
            ship_length=10,
        )

    @classmethod
    def place_carrier(cls):
        return cls(
            ship_length=10,
        )