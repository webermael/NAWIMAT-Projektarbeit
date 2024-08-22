from organisms.sensors import Eyes
from organisms.neural_network import NeuralNetwork
from world.tile import Position
from world.environment import Food, Danger, Empty
from random import randint
import pygame
import math

class Organism:
    def __init__(self, config, x_pos, y_pos, nn = False):
        self.position = Position(x_pos, y_pos)
        self.lifetime = config.organism_start_life # how long the organism will live
        self.alive = True
        self.eyes = Eyes(config.organism_eyes_size)
        self.score = 0
        if nn:
            self.nn = nn
        else:
            self.nn = NeuralNetwork(config.nn_layer_sizes) 
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
        self.lifetime += config.food_bonus

    def move(self, config, direction, world):
        if 0 <= self.position.x + direction[0] < config.row_length and 0 <= self.position.y + direction[1] < config.column_length:
            if not world[self.position.y + direction[1]][self.position.x + direction[0]].has_organism:
                self.position.x += direction[0]
                self.position.y += direction[1]
                if not direction == (0, 0):
                    self.score += config.move_bonus
        else:
            self.lifetime -= config.border_damage
        

    def update_lifetime(self, config):
        self.lifetime -= config.organism_tick_damage
        if self.lifetime <= 0:
            self.alive = False
            self.lifetime = 0
    
    def update(self, config, world):
        world[self.position.y][self.position.x].has_organism = False
        self.move(config, self.directions[self.nn.calc_greatest(self.eyes.sight(config, world, self.position.x, self.position.y))], world)
        world[self.position.y][self.position.x].has_organism = True
        if world[self.position.y][self.position.x].content == "food":
            self.eat(config, world)
        elif world[self.position.y][self.position.x].content == "danger":
            self.lifetime -= config.danger_damage
        self.update_lifetime(config)


    def draw(self, config, display):
        pygame.draw.circle(display, (math.sqrt((255 ** 2 - self.lifetime ** 2 + abs(255 ** 2 - self.lifetime ** 2)) / 2), (255 - math.sqrt((255 ** 2 - self.lifetime ** 2 + abs(255 ** 2 - self.lifetime ** 2)) / 2)) / 2, 255 - math.sqrt((255 ** 2 - self.lifetime ** 2 + abs(255 ** 2 - self.lifetime ** 2)) / 2)), (config.tile_width * (self.position.x + 1 / 2) , config.tile_width * (self.position.y + 1/ 2)), config.tile_width / 2)
