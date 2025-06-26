import math
from dataclasses import dataclass

from src.typedefs import Positionable

@dataclass
class Vec2(Positionable):
    x: float 
    y: float 

    @staticmethod
    def from_p(p: Positionable):
        return Vec2(p.x, p.y)

    def __mul__(self, v: float) -> 'Vec2':
        return Vec2(int(self.x * v), int(self.y * v))

    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)

    def distance(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def norm(self) -> 'Vec2':
        return Vec2(self.x/self.distance(), self.y//self.distance())
