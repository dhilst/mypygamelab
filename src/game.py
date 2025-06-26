from typing import List, Any, Optional, Sequence

import pygame 

from src.env import GridEnvironment
from src.agent import BaseAgent 
from src.color import WHITE, BLACK
from src import mapobjs, utils
from src.typedefs import Drawable

class Game:
    def __init__(self, agents: Sequence[BaseAgent], nobjs=50):
        # Initialize Pygame
        pygame.init()

        # Constants
        self.GRID_SIZE = 32
        self.TILE_SIZE = 20
        self.WINDOW_SIZE = (self.GRID_SIZE * self.TILE_SIZE, self.GRID_SIZE * self.TILE_SIZE)
        self.FPS = 60

        # Setup display
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("Pygame Grid Game")
        self.clock = pygame.time.Clock()

        # Initialize game objects
        self.grid_env = GridEnvironment(self.GRID_SIZE, self.GRID_SIZE)
        self.agents = []
        for agent in agents:
            self._add_agent(agent)

        make_rand_gold = lambda: mapobjs.Gold(
            **utils.random_coord(self.GRID_SIZE, self.GRID_SIZE))
        visited = set()
        for _ in range(0, nobjs):
            mapobj = make_rand_gold()
            while (mapobj.x, mapobj.y) in visited:
                mapobj = make_rand_gold()
            visited.add((mapobj.x, mapobj.y))
            self.grid_env.push_obj(mapobj)
        self.grid_env.push_obj(mapobjs.Dirty(3, 6))
        
        self.running = True

        # Timer for agent action (e.g., every 1 second)
        self.last_agent_time = pygame.time.get_ticks()
        self.agent_interval = 100  # 1000 ms = 1 second

        self.screen.fill(WHITE)

    def _add_agent(self, agent: BaseAgent):
        self.agents.append(agent)
        self.grid_env.push_obj(agent.player)

    def simulate_keypress(self, key: int):
        """
        Simulate a keypress by posting a KEYDOWN event to the Pygame event queue.
        
        Args:
            key (int): Pygame key constant (e.g., pygame.K_UP, pygame.K_DOWN)
        """
        event = pygame.event.Event(pygame.KEYDOWN, key=key)
        pygame.event.post(event)

    def draw_obj(self, obj: Drawable):
        obj.draw(self)

    def draw_grid(self):
        for x in range(self.GRID_SIZE):
            for y in range(self.GRID_SIZE):
                objs = self.grid_env.get_objects_at(x, y)
                if objs:
                    self.draw_obj(objs[-1])
                else:
                    rect = pygame.Rect(x * self.TILE_SIZE, y * self.TILE_SIZE, 
                                       self.TILE_SIZE, self.TILE_SIZE)
                    pygame.draw.rect(self.screen, BLACK, rect, 1)

    def draw(self):
        """Render the game state."""
        
        self.screen.fill(WHITE)
        self.draw_grid()

        pygame.display.flip()

    def run_agent(self, agent: BaseAgent):
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
        
