from typing import Optional, List

from src.player import Player, Action
from src.env import GridEnvironment

import random


class Agent:
    def __init__ (self, player: Player):
        self.player = player

    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        """
        Perceive the environment and player state to decide an action.

        Args:
            environment (GridEnvironment): The game grid environment
            player (Player): The player being controlled

        Returns:
            Optional[int]: A Pygame key constant (e.g., pygame.K_UP) or None if no action
        """
        player = self.player
        # Get valid moves (directions where the player can move)
        valid_moves: List[Action] = []
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

    def act(self, action: Optional[Action], environment: GridEnvironment):
        if action is not None:
            self.player.act(action, environment)
