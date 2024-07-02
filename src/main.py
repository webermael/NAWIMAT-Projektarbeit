import pygame
from config import Config
from world.world import World
#from organisms.organism import Organism
from utils.visualisation import render_world
#from evolution.reproduction import reproduce
#from evolution.mutation import mutate

def main():
    pygame.init()
    config = Config()
    world = World(config)
    #print(world.grid[0][5].position)
    #organisms = [Organism(config) for _ in range(config.num_organisms)]
    
    while True:
        render_world(world)
        break

if __name__ == "__main__":
    main()
