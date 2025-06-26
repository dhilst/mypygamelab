import enum

import pygame

from  typing import final

from src.typedefs import Drawable
from src.env import GridEnvironment
from src.color import Color, BLACK
from src.mapobjs import Dirty, Gold

class Action(str, enum.Enum):
    MOVE_UP = enum.auto()
    MOVE_DOWN = enum.auto()
    MOVE_LEFT = enum.auto()
    MOVE_RIGHT = enum.auto()
    PICK = enum.auto()

class Player:
    def __init__(self, x: int, y: int, color: Color):
        self.x = x
        self.y = y
        self.color = color
        self.score = 0

    def act(self, action: Action, grid_environment: GridEnvironment) -> bool:
        if action == Action.MOVE_UP:
            return self.move_up(grid_environment)
        elif action == Action.MOVE_DOWN:
            return self.move_down(grid_environment)
        elif action == Action.MOVE_LEFT:
            return self.move_left(grid_environment)
        elif action == Action.MOVE_RIGHT:
            return self.move_right(grid_environment)
        elif action == Action.PICK:
            return self.pick(grid_environment)
        else:
            raise ValueError(f"Invalid action {action}")

    def pick(self, grid_environment: GridEnvironment) -> bool:
        x, y = self.x, self.y
        objs = grid_environment.get_objects_except(self)
        for obj in objs:
            if type(obj) is Gold:
                grid_environment.remove_obj(obj)
                self.score += 1
                return True
        return False

    def move_up(self, grid_environment: GridEnvironment) -> bool:
        new_y = self.y - 1
        if grid_environment.is_valid_position(self.x, new_y):
            self.y = new_y
            return True
        return False

    def move_down(self, grid_environment: GridEnvironment) -> bool:
        new_y = self.y + 1
        if grid_environment.is_valid_position(self.x, new_y):
            self.y = new_y
            return True
        return False

    def move_left(self, grid_environment: GridEnvironment) -> bool:
        new_x = self.x - 1
        if grid_environment.is_valid_position(new_x, self.y):
            self.x = new_x
            return True
        return False

    def move_right(self, grid_environment: GridEnvironment) -> bool:
        new_x = self.x + 1
        if grid_environment.is_valid_position(new_x, self.y):
            self.x = new_x
            return True
        return False

    def draw(self, game):
        self_rect = pygame.Rect(
            self.x * game.TILE_SIZE, self.y * game.TILE_SIZE, game.TILE_SIZE, game.TILE_SIZE
        )
        pygame.draw.rect(game.screen, self.color, self_rect)
        font = pygame.font.Font(None, game.TILE_SIZE)
        text = font.render(str(self.score), True, BLACK)
        text_rect = text.get_rect(center=self_rect.center)
        game.screen.blit(text, text_rect)
