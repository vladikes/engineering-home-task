from field import FieldDesigner
from battleship import BattleShip
from fleet import Fleet
import random

def main():
    BATTLEFIELD_CONF = {
        'field_height': 10,
        'field_width': 10,
    }

    BATTLESHIP_PROPERTIES = {
        'submarine': {'length': 1},
        'destroyer': {'length': 2},
        'cruiser': {'length': 3},
        'carrier': {'length': 4},
    }

    battle_field = FieldDesigner()

    battle_field.design_field(
        height=BATTLEFIELD_CONF['field_height'],
        width=BATTLEFIELD_CONF['field_width'],
    )

    submarine = BattleShip(
        ship_length=BATTLESHIP_PROPERTIES['submarine']['length'],
        direction='horizontal',
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='submarine',
    )

    cruiser = BattleShip(
        ship_length=BATTLESHIP_PROPERTIES['cruiser']['length'],
        direction='horizontal',
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='cruiser',
    )

    destroyer = BattleShip(
        ship_length=BATTLESHIP_PROPERTIES['destroyer']['length'],
        direction='horizontal',
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='destroyer',
    )

    carrier = BattleShip(
        ship_length=BATTLESHIP_PROPERTIES['carrier']['length'],
        direction='horizontal',
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='carrier',
    )

    submarine01 = submarine.place_ship()
    cruiser01 = cruiser.place_ship()
    destroyer01 = destroyer.place_ship()
    carrier01 = carrier.place_ship()

    fleet_inventory = Fleet(
        [
         submarine01,
         cruiser01,
         destroyer01,
         carrier01,
         ]
    )


    print(fleet_inventory)
    print(battle_field)


if __name__ == '__main__':
    main()


