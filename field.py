

class FieldDesigner:
    """
    Designs a field for BattleShips
    """
    def __init__(
            self,
    ):
        self.field = []

    def design_field(
            self,
            height,
            width,
    ):

        self.field = [[
                '0' for __
                in range(height)]
                for __ in range(width)
        ]

        return self.field

    def __str__(
            self,
    ):
        return '\n'.join(map(str, self.field))



def main():
    battle_field = FieldDesigner()
    battle_field.design_field(
        height=10,
        width=10,
    )

    print(battle_field)


if __name__ == '__main__':
    main()


