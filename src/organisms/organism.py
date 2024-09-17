from organisms.sensors import Eyes
from organisms.neural_network import NeuralNetwork
from world.tile import Position
from world.environment import Empty
import pygame

class Organism:
    def __init__(self, inputs, x_pos, y_pos, brain_data = False):
        self.position = Position(x_pos, y_pos)
        self.lifetime = inputs["start_life"] # how long the organism will live
        self.alive = True
        self.eyes = Eyes(inputs["eyes_size"]) # maximum number of tiles the organism can see in any direction
        self.score = 0
        if brain_data:
            # takes weights/biases for a network from save file or reproduction
            self.nn = NeuralNetwork(inputs["nn_layer_sizes"], brain_data[0], brain_data[1])
        else:
            # creates a random network if no inputs are given
            # network structure is always the same within a simulation, network values are not
            self.nn = NeuralNetwork(inputs["nn_layer_sizes"]) 
        # used as inputs for the move function, one element is chosen by the network
        self.directions = [(-1, -1),
                        (0, -1),
                        (1, -1),
                        (-1, 0),
                        (0, 0),
                        (1, 0),
                        (-1, 1),
                        (0, 1),
                        (1, 1)] 

    # changes the tile at the current position from food to empty and increases lifetime
    def eat(self, inputs, world):
        world[self.position.y][self.position.x] = Empty(self.position.x, self.position.y)
        self.lifetime += inputs["food"]["lifetime_bonus"]

    # changes the own position
    def move(self, inputs, direction, world):
        if not world[(self.position.y + direction[1]) % inputs["world"]["size"]["column_length"]][(self.position.x + direction[0]) % inputs["world"]["size"]["column_length"]].has_organism:
            # uses modulo to allow movement from one border to the other
            self.position.x = (self.position.x + direction[0]) % inputs["world"]["size"]["row_length"]
            self.position.y = (self.position.y + direction[1]) % inputs["world"]["size"]["column_length"]
            # gives a score bonus for moving
            if not direction == (0, 0):
                self.score += inputs["population"]["interactions"]["move_bonus"]
        
    # updates lifetime and kills the organism if lifetime is zero
    def update_lifetime(self):
        self.lifetime -= 1
        if self.lifetime <= 0:
            self.alive = False
            self.lifetime = 0
    
    # updates the organisms position, lifetime and has_organism values of tiles it interacts with
    def update(self, inputs, world):
        world[self.position.y][self.position.x].has_organism = False
        self.move(inputs, self.directions[self.nn.calc_greatest(self.eyes.sight(inputs["world"]["size"], world, self.position.x, self.position.y))], world)
        world[self.position.y][self.position.x].has_organism = True

        if world[self.position.y][self.position.x].content == "food":
            self.eat(inputs["world"], world)
        elif world[self.position.y][self.position.x].content == "danger":
            self.lifetime -= inputs["world"]["danger"]["damage"]
        self.update_lifetime()

    #draws a blue circle
    def draw(self, tile_width, display):
        pygame.draw.circle(display, (0, 80, 230), (tile_width * (self.position.x + 1 / 2) , tile_width * (self.position.y + 1/ 2)), tile_width / 1.5)
