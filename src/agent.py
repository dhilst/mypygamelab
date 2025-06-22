from typing import Optional, List
import random

from src.player import Player, Action
from src.env import GridEnvironment
from src.mapobjs import Dirty


class BaseAgent:
    def __init__ (self, player: Player):
        self.player = player

    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        return None

    def act(self, action: Optional[Action], environment: GridEnvironment):
        if action is not None:
            self.player.act(action, environment)

class RandomAgent(BaseAgent):
    def __init__ (self, player: Player):
        self.player = player

    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        valid_moves: List[Action] = []
        player = self.player
        observed = environment.get_objects_except(player)
        if observed:
            if type(observed[-1]) is Dirty:
                return Action.CLEAN_UP
        # Get valid moves (directions where the player can move)
        if environment.is_valid_position(player.x, player.y - 1):
            valid_moves.append(Action.MOVE_UP)
        if environment.is_valid_position(player.x, player.y + 1):
            valid_moves.append(Action.MOVE_DOWN)
        if environment.is_valid_position(player.x - 1, player.y):
            valid_moves.append(Action.MOVE_LEFT)
        if environment.is_valid_position(player.x + 1, player.y):
            valid_moves.append(Action.MOVE_RIGHT)

        # Choose a random valid move, or None if no moves are possible
        return random.choice(valid_moves) if valid_moves else None

class RightAgent(BaseAgent):
    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        return Action.MOVE_RIGHT

