
import random
from fleet import Ship


class BattleShip:
    """
    Accepts battleship parameters and deploys ships as well as sets the shape of the ship.
    """
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

        # Checks if ship is off border and if vertical or horizontal
        deployment_attempts = 0
        while deployment_attempts < 10:
            deployment_attempts += 1

            if self.direction == 'vertical':

                if x <= min_field_grid \
                        or x + self.ship_length > self.max_field_grid \
                        or y <= min_field_grid \
                        or y >= self.max_field_grid:

                    print('Ship is off border, re-deploying')
                    continue

                for i in self.field.field[y:y + self.ship_length]:
                    i[x] = self.SHIPS_SHAPE
            else:

                if x <= min_field_grid \
                        or x + self.ship_length > self.max_field_grid \
                        or y <= min_field_grid \
                        or y >= self.max_field_grid:

                    print('Ship is off border, re-deploying')
                    continue

                self.field.field[y][x: x + self.ship_length] = [
                    self.SHIPS_SHAPE
                    for i in
                    range(self.ship_length)
                ]

            return Ship(
                position=[x, y],
                length=self.ship_length,
                direction=self.direction,
                type=self.type,
            )