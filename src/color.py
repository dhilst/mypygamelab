from typing import NamedTuple

class Color(NamedTuple):
    """A named tuple representing an RGB color."""
    red: int
    green: int
    blue: int

WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)
BROWN = Color(red=150, green=75, blue=0)
BLUE = Color(red=0, green=0, blue=255)
GREEN = Color(red=0, green=255, blue=0)
