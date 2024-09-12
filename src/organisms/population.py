from organisms.organism import Organism
from organisms.neural_network import NeuralNetwork
from random import randint

class Population:
    def __init__(self, inputs, world_sizes):
        self.organisms = []
        self.organism_coords = []
        while len(self.organisms) < inputs["population_size"]:
            coords = (randint(0, world_sizes["row_length"] - 1), randint(0, world_sizes["column_length"] - 1))
            if coords not in self.organism_coords:
                if inputs["organisms"]["networks"]:
                    nn = NeuralNetwork(inputs["organisms"]["nn_layer_sizes"], 
                                       inputs["organisms"]["networks"][len(self.organisms)]["weights"],
                                       inputs["organisms"]["networks"][len(self.organisms)]["biases"])
                    self.organisms.append(Organism(inputs["organisms"], coords[0], coords[1], nn))
                else:
                    self.organisms.append(Organism(inputs["organisms"], coords[0], coords[1]))
                self.organism_coords.append(coords)
    
    def draw(self, tile_width, display):
        for organism in self.organisms:
            if organism.alive:
                organism.draw(tile_width, display)
    
    def update(self, inputs, world):
        for organism in self.organisms:
            if organism.alive:
                organism.update(inputs, world)
            else:
                world[organism.position.y][organism.position.x].has_organism = False

    def update_lifetime(self):
        for organism in self.organisms:
            if organism.alive:
                organism.update_lifetime()
    