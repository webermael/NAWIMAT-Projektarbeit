from organisms.sensors import Eyes
from organisms.neural_network import NeuralNetwork
from world.tile import Position
from world.environment import Food, Danger, Empty
from random import randint
import pygame

class Organism:
    def __init__(self, inputs, x_pos, y_pos, nn = False):
        self.position = Position(x_pos, y_pos)
        self.lifetime = inputs["start_life"] # how long the organism will live
        self.alive = True
        self.eyes = Eyes(inputs["eyes_size"])
        self.score = 0
        if nn:
            self.nn = nn
        else:
            self.nn = NeuralNetwork(inputs["nn_layer_sizes"]) 
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

    def eat(self, inputs, world):
        world[self.position.y][self.position.x] = Empty(inputs["size"]["tile_width"], self.position.x, self.position.y)
        self.lifetime += inputs["food"]["lifetime_bonus"]

    def move(self, inputs, direction, world):
        if 0 <= self.position.x + direction[0] < inputs["world"]["size"]["row_length"] and 0 <= self.position.y + direction[1] < inputs["world"]["size"]["column_length"]:
            if not world[self.position.y + direction[1]][self.position.x + direction[0]].has_organism:
                self.position.x += direction[0]
                self.position.y += direction[1]
                if not direction == (0, 0):
                    self.score += inputs["population"]["interactions"]["move_bonus"]
        else:
            self.lifetime -= inputs["population"]["interactions"]["border_damage"]
        

    def update_lifetime(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.alive = False
            self.lifetime = 0
    
    def update(self, inputs, world):
        world[self.position.y][self.position.x].has_organism = False
        self.move(inputs, self.directions[self.nn.calc_greatest(self.eyes.sight(inputs["world"]["size"], world, self.position.x, self.position.y))], world)
        world[self.position.y][self.position.x].has_organism = True
        if world[self.position.y][self.position.x].content == "food":
            self.eat(inputs["world"], world)
        elif world[self.position.y][self.position.x].content == "danger":
            self.lifetime -= inputs["world"]["danger"]["damage"]
        self.update_lifetime()


    def draw(self, tile_width, display):
        pygame.draw.circle(display, (0, 80, 230), (tile_width * (self.position.x + 1 / 2) , tile_width * (self.position.y + 1/ 2)), tile_width / 1.5)
