#import pygame
#from config import Config
#from world.world import World
#from organisms.population import Population
#from utils.visualisation import (render_world, screen_init, screen_update)
#from evolution.reproduction import reproduce
#from evolution.mutation import mutate
from simulation import Simulation
from utils.file_manager import FileManager

def main():
    fm = FileManager()
    load_dict = fm.load_file("template.json")
    simulation = Simulation(load_dict)

    simulation.evolve()
    
    dict = fm.sim_to_dict(load_dict, simulation)
    fm.save_dict("save.json", dict)

if __name__ == "__main__":
    main()
