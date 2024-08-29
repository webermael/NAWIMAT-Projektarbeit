from organisms.organism import Organism
from organisms.neural_network import NeuralNetwork
from random import randint

class Population:
    def __init__(self, config, network_dict = False):
        self.organisms = []
        self.organism_coords = []
        while len(self.organisms) < config.population_size:
            coords = (randint(0, config.row_length - 1), randint(0, config.column_length - 1))
            if coords not in self.organism_coords:
                if network_dict:
                    nn = NeuralNetwork(config.nn_layer_sizes, 
                                       network_dict["organisms"][len(self.organisms)]["network_weights"],
                                       network_dict["organisms"][len(self.organisms)]["network_biases"])
                    self.organisms.append(Organism(config, coords[0], coords[1], nn))
                else:
                    self.organisms.append(Organism(config, coords[0], coords[1]))
                self.organism_coords.append(coords)
    
    def draw(self, config, display):
        for organism in self.organisms:
            if organism.alive:
                organism.draw(config, display)
    
    def update(self, config, world):
        for organism in self.organisms:
            if organism.alive:
                organism.update(config, world)
            else:
                world[organism.position.y][organism.position.x].has_organism = False

    def update_lifetime(self):
        for organism in self.organisms:
            if organism.alive:
                organism.update_lifetime()
    