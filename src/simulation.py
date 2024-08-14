import pygame
from config import Config
from world.world import World
from organisms.population import Population
from utils.visualisation import (render_world, screen_init, screen_update)


class Simulation():
    def __init__(self):
        self.config = Config()
        self.generation_duration = self.config.generation_duration
        self.world = World(self.config)
        self.population = Population(self.config)
        self.screen = screen_init(self.config)
        self.running = True
    
    def run(self):
        pygame.init()
        while self.generation_duration > 0 and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.running = False
            self.screen.fill((255, 255, 255))

            self.world.spread(self.config)
            self.world.draw(self.config, self.screen)
            self.population.update(self.config, self.world.grid)
            self.population.draw(self.config, self.screen)
            # drawing everything

            screen_update()
            self.generation_duration -= 1
            pygame.time.Clock().tick(60)
        pygame.quit()
    
    def reset(self):
        self.generation_duration = self.config.generation_duration
        self.world = World(self.config)
        self.population = Population(self.config)
        self.screen = screen_init(self.config)
    
    def evolve(self):
        while self.running:
            self.run()
            self.reset()
