class FieldDesigner:
    """
    Designs a field for BattleShips, accepts field height and width
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
                '~' for __
                in range(height)]
                for __ in range(width)
        ]

        return self.field

    def __str__(
            self,
    ):
        return '\n'.join(map(str, self.field))