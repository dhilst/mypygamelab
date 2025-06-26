from typing import Sequence

from src.game import Game
from src.player import Player
from src.agent import BaseAgent, RandomAgent, RightAgent, SearchAgent, SearchClosestAgent
from src import color

def main():
    agents= [
             RandomAgent(Player(0, 0, color.BLUE)),
             SearchAgent(Player(5, 5, color.RED)),
             RightAgent(Player(3, 3, color.GREEN)),
             SearchClosestAgent(Player(7, 7, color.PINK)),
             ]
    game = Game(agents)
    game.run()

if __name__ == "__main__":
    main()
