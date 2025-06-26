from typing import Protocol

from src.color import Color


class Positionable(Protocol):
    x: int
    y: int


class Drawable(Positionable):
    color: Color

    def draw(self, game): ...



class Player(Drawable):
    pass


class Agent(Protocol):
    player: Player
