from typing import Protocol

class Positionable(Protocol):
    @property
    def x(self) -> int: ...

    @property
    def y(self) -> int: ...

