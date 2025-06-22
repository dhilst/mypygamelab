import enum

from src.env import GridEnvironment
from src.color import Color

class Action(str, enum.Enum):
    MOVE_UP = enum.auto()
    MOVE_DOWN = enum.auto()
    MOVE_LEFT = enum.auto()
    MOVE_RIGHT = enum.auto()

class Player:
    def __init__(self, x: int, y: int, color: Color):
        self.x = x
        self.y = y
        self.color = color

    def act(self, action: Action, grid_environment: GridEnvironment) -> bool:
        if action == Action.MOVE_UP:
            return self.move_up(grid_environment)
        elif action == Action.MOVE_DOWN:
            return self.move_down(grid_environment)
        elif action == Action.MOVE_LEFT:
            return self.move_left(grid_environment)
        elif action == Action.MOVE_RIGHT:
            return self.move_right(grid_environment)
        else:
            raise ValueError(f"Invalid action {action}")

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

