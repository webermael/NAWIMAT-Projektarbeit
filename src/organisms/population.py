from organisms.organism import Organism
from random import randint

class Population:
    '''
    creates a population of organisms
    creates their networks randomly or takes them from a save file
    used to update and draw all organisms
    '''
    def __init__(self, inputs, world_sizes, coords_only = False):
        self.organisms = []
        self.organism_coords = []
        if inputs["population_size"] > int(world_sizes["row_length"] * world_sizes["column_length"] // 1.25):
            inputs["population_size"] = int(world_sizes["row_length"] * world_sizes["column_length"] // 1.25)
        while len(self.organism_coords) < inputs["population_size"]:
            # creates random untaken coordinates until the list length equals population_size 
            coords = (randint(0, world_sizes["row_length"] - 1), randint(0, world_sizes["column_length"] - 1))
            if coords not in self.organism_coords:
                if inputs["organisms"]["networks"] and not coords_only:
                    if len(self.organisms) < len(inputs["organisms"]["networks"]):
                        # takes the next network from a save 
                        brain_index = len(self.organisms)
                    else:
                        # takes a random network from the input
                        # if population size is bigger than the number of input networks
                        brain_index = randint(0, len(inputs["organisms"]["networks"]) - 1)
                    # creates an organism with the input network
                    self.organisms.append(Organism(inputs["organisms"], coords[0], coords[1],
                                            (inputs["organisms"]["networks"][brain_index]["weights"],
                                            inputs["organisms"]["networks"][brain_index]["biases"])))
                elif not inputs["organisms"]["networks"] and not coords_only:
                    self.organisms.append(Organism(inputs["organisms"], coords[0], coords[1]))
                # can generate only coordinates to not waste organism objects in the simulation reset
                self.organism_coords.append(coords)
    
    # draws every organism
    def draw(self, tile_width, display):
        for organism in self.organisms:
            if organism.alive:
                organism.draw(tile_width, display)
    
    # update every organism, set has_organism to false on a tile where an organism dies
    def update(self, inputs, world):
        for organism in self.organisms:
            if organism.alive:
                organism.update(inputs, world)
            else:
                world[organism.position.y][organism.position.x].has_organism = False

    