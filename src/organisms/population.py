from organisms.organism import Organism
from random import randint

class Population:
    def __init__(self, config):
        self.organisms = [Organism(config, randint(0, config.row_length), randint(0, config.column_length)) for i in range(config.population_size)]
    
    def draw(self, config, display):
        for organism in self.organisms:
            organism.draw(config, display)
    
    def update(self, config):
        for organism in self.organisms:
            organism.update(config)
            if not organism.alive:
                self.organisms.remove(organism)
    

    def update_lifetime(self):
        for organism in self.organisms:
            organism.update_lifetime()
    