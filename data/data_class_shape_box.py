from dataclasses import dataclass


@dataclass
class ShapeBox:
    left: int
    bottom: int
    right: int
    top: int
