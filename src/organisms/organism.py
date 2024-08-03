#from src.organisms.sensors import Sensor
from organisms.neural_network import NeuralNetwork
from world.tile import Position
from random import randint
import pygame

class Organism:
    def __init__(self, config, x_pos, y_pos):
        self.position = Position(x_pos, y_pos)
        self.vitality = randint(config.organism_min_vit, config.organism_max_vit) # current state of wellbeing, used to reduce lifetime more/less, randomized at the beginning
        self.lifetime = randint(config.organism_min_life, config.organism_max_life) # how long the organism will live, randomized
        self.alive = True
        self.nn = NeuralNetwork((1, 3, 9)) 
        # Inputs will later be determined by the tiles the organism "sees" through the sensors class
        # Hidden Layers will be randomized or set the same for every organism at the beginning and later changed through mutations
        # One output for every action an organism can do, at the moment it's moving to any adjacent tile including the current one
        self.directions = [(-1, -1),
                        (0, -1),
                        (1, -1),
                        (-1, 0),
                        (0, 0),
                        (1, 0),
                        (-1, 1),
                        (0, 1),
                        (1, 1)] # used as inputs for the move function, one element for moving to one of the adjacent tiles

    def move(self, direction, config):
        self.position.x += direction[0]
        self.position.y += direction[1]

        if self.position.x > config.row_length - 1: # stop organsims from exiting the screen from left/rigth
            self.position.x = config.row_length - 1
        elif self.position.x < 0:
            self.position.x = 0
        
        if self.position.y > config.column_length - 1: # stop organsims from exiting the screen from top/bottom
            self.position.y = config.column_length - 1
        elif self.position.y < 0:
            self.position.y = 0

    def update_lifetime(self):
        self.lifetime -= 100 / self.vitality
        if self.lifetime <= 0:
            self.alive = False
    
    def update(self, config):
        self.move(self.directions[self.nn.calc_greatest([randint(0, 10)])], config)
        # self.update_lifetime()


    def draw(self, config, display):
        pygame.draw.circle(display, (0, 0, 0), (config.tile_width * (self.position.x + 1 / 2) , config.tile_width * (self.position.y + 1/ 2)), config.tile_width / 2)

    def checktile(self, world):
        tile_type = world[self.position.y][self.position.x].type
        if tile_type == "empty":
            ...
        elif tile_type == "food":
            ...
        elif tile_type == "danger":
            ...
