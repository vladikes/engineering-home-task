from field import FieldDesigner
from battleship import BattleShip


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

    ship_dispatcher = BattleShip(
        length=BATTLESHIP_PROPERTIES['submarine']['length'],
        direction=None,
    )


    print(ship_dispatcher.place_submarine())
    print(battle_field)

if __name__ == '__main__':
    main()


