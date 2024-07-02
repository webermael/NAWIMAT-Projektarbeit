import pygame
from config import Config
from world.world import World
#from src.organisms.organism import Organism
#from src.world.tiles import Tile
#from src.evolution.reproduction import reproduce
#from src.evolution.mutation import mutate

def main():
    #pygame.init()
    config = Config()
    world = World(config)
    print(world.grid)
    #organisms = [Organism(config) for _ in range(config.num_organisms)]
    
    #while True:
        # Update and render
    #    pass

if __name__ == "__main__":
    main()
