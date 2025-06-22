from typing import Sequence

from src.game import Game
from src.player import Player
from src.agent import BaseAgent, RandomAgent, RightAgent
from src import color

def main():
    agents= [
             BaseAgent(Player(0, 1, color.RED)),
             RandomAgent(Player(0, 0, color.RED)),
             RandomAgent(Player(5, 5, color.BLUE)),
             RightAgent(Player(3, 3, color.GREEN)),
             ]
    game = Game(agents)
    game.run()

if __name__ == "__main__":
    main()
