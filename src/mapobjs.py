import pygame
from src.typedefs import Drawable 
from src.color import BROWN, YELLOW

class Dirty(Drawable):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.color = BROWN 

    def draw(self, game):
        self_rect = pygame.Rect(
            self.x * game.TILE_SIZE, self.y * game.TILE_SIZE, game.TILE_SIZE, game.TILE_SIZE
        )
        pygame.draw.rect(game.screen, self.color, self_rect)

class Gold(Drawable):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.color = YELLOW

    def draw(self, game):
        self_rect = pygame.Rect(
            self.x * game.TILE_SIZE, self.y * game.TILE_SIZE, game.TILE_SIZE, game.TILE_SIZE
        )
        pygame.draw.circle(game.screen, self.color, (self_rect.centerx, self_rect.centery), game.TILE_SIZE / 2 - 2, width=0)
