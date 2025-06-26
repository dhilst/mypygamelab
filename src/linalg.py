import math
from dataclasses import dataclass

from src.typedefs import Positionable

@dataclass
class Vec2(Positionable):
    """
    Integer precision vector for positioning computations
    """
    x: int 
    y: int

    @staticmethod
    def from_p(p: Positionable):
        return Vec2(p.x, p.y)

    def __mul__(self, v: int) -> 'Vec2':
        return Vec2(self.x * v, self.y * v)

    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)

    def distance(self) -> int:
        return int(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

    def norm(self) -> 'Vec2':
        return Vec2(self.x//self.distance(), self.y//self.distance())
