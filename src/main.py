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
    FM = FileManager()
    simulation = Simulation(FM.load_file("input.json"))
    simulation.evolve()
    save = {}
    save["generation_counter"] = simulation.generation_counter
    save["organisms"] = [{"network_weights" : 
                            [layer.weights for layer in simulation.population.organisms[organism].nn.layers], 
                            
                            "network_biases" : 
                            [layer.biases for layer in simulation.population.organisms[organism].nn.layers]} 
                            
                            for organism in range(len(simulation.population.organisms))
                            ]

    FM.save_dict("save.json", save)

if __name__ == "__main__":
    main()
