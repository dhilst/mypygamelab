from src.typedefs import Drawable 
from src.color import BROWN

class Dirty(Drawable):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.color = BROWN 
