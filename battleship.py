import random
from fleet import Ship
from random import randint


class BattleShip:
    SHIPS_SHAPE = '#'

    def __init__(
            self,
            ship_length,
            direction,
            max_field_grid,
            field,
            type,
    ):
        self.ship_length = ship_length
        self.direction = direction
        self.max_field_grid = max_field_grid
        self.field = field
        self.type = type

    def place_ship(
            self,
    ):
        min_field_grid = 1
        x = random.choice(
            range(
                min_field_grid,
                self.max_field_grid,
            )
        )

        y = random.choice(
            range(
                min_field_grid,
                self.max_field_grid,
            )
        )

        for i in self.field.field[y:y + self.ship_length]:
            i[x] = self.SHIPS_SHAPE

        return Ship(
            position=[x, y],
            length=self.ship_length,
            direction=self.direction,
            type=self.type,
        )