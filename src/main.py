import pygame
from config import Config
from world.world import World
from organisms.population import Population
from utils.visualisation import (render_world, screen_init, screen_update)
#from evolution.reproduction import reproduce
#from evolution.mutation import mutate

def main():
    pygame.init()
    config = Config()
    world = World(config)
    population = Population(config)
    screen = screen_init(config)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
        screen.fill((255, 255, 255))

        world.draw(config, screen)
        # world.spread(config)
        population.draw(config, screen)
        population.update(config)
        # drawing everything

        screen_update()
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
