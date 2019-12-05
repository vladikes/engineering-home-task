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
            place=None,
    ):
        self.ship_length = ship_length
        self.direction = direction
        self.max_field_grid = max_field_grid
        self.field = field
        self.type = type
        self.place = place

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

        return self.field, Ship(
            field=self.field,
            position=[x, y],
            length=self.ship_length,
            direction=self.direction,
            type=self.type,
            place = self.place
        )