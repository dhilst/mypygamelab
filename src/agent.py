import math
from os import environ
from typing import Optional, List
import random

from src.player import Player, Action
from src.env import GridEnvironment
from src.mapobjs import Gold
from src.linalg import Vec2


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
            if type(observed[-1]) is Gold:
                return Action.PICK
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


class SearchAgent(RandomAgent):
    def find_gold(self, objs):
        for obj in objs:
            if type(obj) is Gold:
                return obj
        return None

    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        player = self.player
        for x, y, objs in environment:
            gold = self.find_gold(objs)
            if gold is None:
                continue

            if player.x < x:
                return Action.MOVE_RIGHT
            elif player.x > x:
                return Action.MOVE_LEFT

            if player.y < y:
                return Action.MOVE_DOWN
            elif player.y > y:
                return Action.MOVE_UP

            assert(player.x == x and player.y == y)
            return Action.PICK

        return super().perceive(environment)

class SearchClosestAgent(RandomAgent):
    def find_closest_gold(self, env: GridEnvironment):
        min_distance = float(max(env.width, env.height) + 1)
        closest_gold = None
        from collections import namedtuple
        vec2 = namedtuple('vec2', 'x y')
        def diff(v1, v2):
            return vec2(v1.x - v2.x, v1.y - v2.y)
        def mag(v1) -> float:
            return math.sqrt(v1.x**2 + v1.y**2)
        for _, _, objs in env:
            for gold in objs:
                if not type(gold) is Gold:
                    continue
                direction = diff(gold, self.player)
                dist = mag(direction)
                if dist < min_distance:
                    min_distance = dist
                    closest_gold = gold

        return closest_gold

    def perceive(self, environment: GridEnvironment) -> Optional[Action]:
        player = self.player
        gold = self.find_closest_gold(environment)
        if gold is None:
            # Nothing to do
            return None

        x = gold.x
        y = gold.y
        if player.x < x:
            return Action.MOVE_RIGHT
        elif player.x > x:
            return Action.MOVE_LEFT

        if player.y < y:
            return Action.MOVE_DOWN
        elif player.y > y:
            return Action.MOVE_UP

        assert(player.x == x and player.y == y)
        return Action.PICK
