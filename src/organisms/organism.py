#from src.organisms.sensors import Sensor
#from src.organisms.neural_network import NeuralNetwork
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
        #self.nn = NeuralNetwork(config)

    def move(self, direction):
        self.position.x += direction[0]
        self.position.y += direction[1]

    def update_lifetime(self):
        self.lifetime -= 100 / self.vitality
        if self.lifetime <= 0:
            self.alive = False
    
    def draw(self, config, display):
        pygame.draw.circle(display, (255, 0, 0), (self.position.x * config.tile_width, self.position.y * config.tile_width), config.tile_width / 2)

    def vision(self):
         view = [World.grid[self.position.y - 2][self.position.x - i for i in range ( -2, 3)].content, 
            World.grid[self.position.y - 1][self.position.x - i for i in range ( -2, 3)].content, 
            World.grid[self.position.y][self.position.x - i for i in range ( -2, 3)].content,
            World.grid[self.position.y + 1][self.position.x - i for i in range ( -2, 3)].content,
            World.grid[self.position.y + 2][self.position.x - i for i in range ( -2, 3)].content]
        return view
    
        
                
        
