from dataclasses import dataclass, field

"""
Holds ship information and fleet object dataclasses
"""
@dataclass
class Ship:
    type: str = None
    direction: str = None
    position: list = field(
        default_factory=list,
    )
    length: int = 0


@dataclass
class Fleet:
    Ships: field(
        default_factory=list,
    )