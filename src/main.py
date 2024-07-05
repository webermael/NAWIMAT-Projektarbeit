import pygame
from config import Config
from world.world import World
#from organisms.organism import Organism
from utils.visualisation import (render_world, screen_init, screen_update) 
#from evolution.reproduction import reproduce
#from evolution.mutation import mutate

def main():
    pygame.init()
    config = Config()
    world = World(config)
    #organisms = [Organism(config) for _ in range(config.num_organisms)]
    screen = screen_init(config)
    while True:
        render_world(world)
        screen_update()
        break

if __name__ == "__main__":
    main()
