#from src.organisms.sensors import Sensor
#from src.organisms.neural_network import NeuralNetwork
from world.tile import Position

class Organism:
    def __init__(self, config, x_pos, y_pos):
        self.position = Position(x_pos, y_pos)
        self.vitality = config.organism_vitality # current state of wellbeing, used to reduce lifetime more/less
        self.lifetime = config.organism_lifetime # how long the organism will live
        self.alive = True
        #self.nn = NeuralNetwork(config)

    def move(self, world, direction):
        self.position.x += direction[0]
        self.position.y += direction[1]

    def update_lifetime(self):
        self.lifetime -= 100 / self.vitality
        if self.lifetime <= 0:
            self.alive = False
    
    def checktile(self, world):
        tile_type = world[self.position.y][self.position.x].type
        if tile_type == "empty":
            ...
        elif tile_type == "food":
            ...
        elif tile_type == "danger":
            ...
