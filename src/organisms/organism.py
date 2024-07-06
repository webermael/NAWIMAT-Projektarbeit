#from src.organisms.sensors import Sensor
#from src.organisms.neural_network import NeuralNetwork
from world.tile import Position
from random import randint
import pygame

class Organism:
    def __init__(self, config):
        self.position = Position(randint(0, config.row_length), randint(0, config.column_length))
        self.vitality = randint(config.organism_min_vit, config.organism_max_vit) # current state of wellbeing, used to reduce lifetime more/less, randomized at the beginning
        self.lifetime = randint(config.organism_min_life, config.organism_max_life) # how long the organism will live, randomized
        self.alive = True
        #self.nn = NeuralNetwork(config)

    def move(self, world, direction):
        self.position.x += direction[0]
        self.position.y += direction[1]

    def update_lifetime(self):
        self.lifetime -= 100 / self.vitality
        if self.lifetime <= 0:
            self.alive = False
    
    def draw(self, config, display):
        pygame.draw.circle(display, (255, 0, 0), (self.position.x * config.tile_width, self.position.y * config.tile_width), config.tile_width / 2)

    def checktile(self, world):
        tile_type = world[self.position.y][self.position.x].type
        if tile_type == "empty":
            ...
        elif tile_type == "food":
            ...
        elif tile_type == "danger":
            ...
