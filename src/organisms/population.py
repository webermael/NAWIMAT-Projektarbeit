from organisms.organism import Organism
from random import randint

class Population:
    def __init__(self, config):
        self.organisms = []
        self.organism_coords = []
        while len(self.organisms) < config.population_size:
            coords = (randint(0, config.row_length - 1), randint(0, config.column_length - 1))
            if coords not in self.organism_coords:
                self.organisms.append(Organism(config, coords[0], coords[1]))
                self.organism_coords.append(coords)
    
    def draw(self, config, display):
        for organism in self.organisms:
            if organism.alive:
                organism.draw(config, display)
    
    def update(self, config, grid):
        for organism in self.organisms:
            if organism.alive:
                organism.update(config, grid)
            else:
                grid[organism.position.y][organism.position.x].has_organism = False

    def update_lifetime(self):
        for organism in self.organisms:
            if organism.alive:
                organism.update_lifetime()
    