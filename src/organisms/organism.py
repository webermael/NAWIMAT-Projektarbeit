from organisms.sensors import Eyes
from organisms.neural_network import NeuralNetwork
from world.tile import Position
from world.environment import Food, Danger, Empty
from random import randint
import pygame

class Organism:
    def __init__(self, config, x_pos, y_pos):
        self.position = Position(x_pos, y_pos)
        self.vitality = randint(config.organism_min_vit, config.organism_max_vit) # current state of wellbeing, used to reduce lifetime more/less, randomized at the beginning
        self.lifetime = randint(config.organism_min_life, config.organism_max_life) # how long the organism will live, randomized
        self.alive = True
        self.eyes = Eyes(2)
        self.nn = NeuralNetwork(((self.eyes.size * 2 + 1) ** 2, 5, 9)) 
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

    def eat(self, config, world):
        world[self.position.y][self.position.x] = Empty(config, self.position.x, self.position.y)

    def move(self, config, direction, world):
        if 0 <= self.position.x + direction[0] < config.row_length and 0 <= self.position.y + direction[1] < config.column_length:
            if not world[self.position.y + direction[1]][self.position.x + direction[0]].has_organism:
                self.position.x += direction[0]
                self.position.y += direction[1]

    def update_lifetime(self):
        self.lifetime -= 100 / self.vitality
        if self.lifetime <= 0:
            self.alive = False
    
    def update(self, config, world):
        world[self.position.y][self.position.x].has_organism = False
        self.move(config, self.directions[self.nn.calc_greatest(self.eyes.sight(config, world, self.position.x, self.position.y))], world)
        world[self.position.y][self.position.x].has_organism = True
        if world[self.position.y][self.position.x].content == "food":
            self.eat(config, world)
        # self.update_lifetime()


    def draw(self, config, display):
        pygame.draw.circle(display, (0, 0, 0), (config.tile_width * (self.position.x + 1 / 2) , config.tile_width * (self.position.y + 1/ 2)), config.tile_width / 2)
