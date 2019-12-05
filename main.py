from field import FieldDesigner
from battleship import BattleShip
from fleet import Fleet


def main():
    """
    Holds battlefield and fleet properties as well as field and battleship classes.
    """
    BATTLEFIELD_CONF = {
        'field_height': 10,
        'field_width': 10,
    }

    FLEET_PROPERTIES = {
        'submarine': {'length': 1, 'direction': None, },
        'destroyer': {'length': 2, 'direction': 'horizontal', },
        'cruiser': {'length': 3, 'direction': 'horizontal', },
        'carrier': {'length': 4, 'direction': 'vertical', },
    }

    battle_field = FieldDesigner()

    battle_field.design_field(
        height=BATTLEFIELD_CONF['field_height'],
        width=BATTLEFIELD_CONF['field_width'],
    )

    submarine = BattleShip(
        ship_length=FLEET_PROPERTIES['submarine']['length'],
        direction=FLEET_PROPERTIES['submarine']['direction'],
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='submarine',
    )

    cruiser = BattleShip(
        ship_length=FLEET_PROPERTIES['cruiser']['length'],
        direction=FLEET_PROPERTIES['cruiser']['direction'],
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='cruiser',
    )

    destroyer = BattleShip(
        ship_length=FLEET_PROPERTIES['destroyer']['length'],
        direction=FLEET_PROPERTIES['destroyer']['direction'],
        field=battle_field,
        max_field_grid=BATTLEFIELD_CONF['field_width'],
        type='destroyer',
    )

    carrier = BattleShip(
        ship_length=FLEET_PROPERTIES['carrier']['length'],
        direction=FLEET_PROPERTIES['carrier']['direction'],
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


