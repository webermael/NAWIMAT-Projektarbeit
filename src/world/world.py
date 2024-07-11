from world.tile import Tile
from world.environment import Danger
from random import randint

class World:
    def __init__(self, config):
        self.width = config.row_length
        self.height = config.column_length
        self.grid = [[Tile(config, x_pos, y_pos) for x_pos in range(self.width)] for y_pos in range(self.height)]
    
    def draw(self, config, display):
        for column in self.grid:
            for tile in column:
                tile.draw(config, display)
    
    def spread(self, config):
        for column in self.grid:
            for tile in column:
                if tile.content == "danger":
                    tile.spread(self.grid, config)
