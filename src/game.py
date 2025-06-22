from typing import List, Any, Optional

import pygame 

from src.agent import Agent
from src.player import Player
from src.env import GridEnvironment
from src.color import Color, WHITE, RED, BLACK, BLUE

class Game:
    def _add_player(self, x: int, y: int, color: Color):
        player = Player(x, y, color)
        agent = Agent(player)
        self.players.append(player)
        self.agents.append(agent)
        self.grid_env.push_obj(player)

    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.GRID_SIZE = 16
        self.TILE_SIZE = 40
        self.WINDOW_SIZE = (self.GRID_SIZE * self.TILE_SIZE, self.GRID_SIZE * self.TILE_SIZE)
        self.FPS = 60

        # Setup display
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Pygame Grid Game")
        self.clock = pygame.time.Clock()

        # Initialize game objects
        self.grid_env = GridEnvironment()
        self.players = []
        self.agents = []
        self._add_player(0, 0, RED)
        self._add_player(5, 5, BLUE)
        
        self.running = True

        # Timer for agent action (e.g., every 1 second)
        self.last_agent_time = pygame.time.get_ticks()
        self.agent_interval = 100  # 1000 ms = 1 second

        self.screen.fill(WHITE)

    def simulate_keypress(self, key: int):
        """
        Simulate a keypress by posting a KEYDOWN event to the Pygame event queue.
        
        Args:
            key (int): Pygame key constant (e.g., pygame.K_UP, pygame.K_DOWN)
        """
        event = pygame.event.Event(pygame.KEYDOWN, key=key)
        pygame.event.post(event)

    def draw_players(self):
        for player in self.players:
            player_rect = pygame.Rect(
                player.x * self.TILE_SIZE, player.y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE
            )
            pygame.draw.rect(self.screen, player.color, player_rect)

    def draw_grid(self):
        # Draw grid
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                rect = pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE)
                pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw(self):
        """Render the game state."""
        
        # self.screen.fill(WHITE)
        self.draw_grid()
        self.draw_players()

        pygame.display.flip()

    def run_agent(self, agent: Agent):
        action = agent.perceive(self.grid_env)
        agent.act(action, self.grid_env)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


    def run(self):
        """Main game loop."""
        while self.running:
            # Let agent perceive and act periodically
            current_time = pygame.time.get_ticks()
            if current_time - self.last_agent_time >= self.agent_interval:
                for agent in self.agents:
                    self.run_agent(agent)
                self.last_agent_time = current_time

            self.handle_events()
            self.draw()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        
