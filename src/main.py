#import pygame
#from config import Config
#from world.world import World
#from organisms.population import Population
#from utils.visualisation import (render_world, screen_init, screen_update)
#from evolution.reproduction import reproduce
#from evolution.mutation import mutate
from simulation import Simulation

def main():
    simulation = Simulation()
    simulation.evolve()

if __name__ == "__main__":
    main()
