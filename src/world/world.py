from world.tile import Tile
from world.environment import Danger, Food, Empty
from random import randint

class World:
    def __init__(self, config):
        self.width = config.row_length
        self.height = config.column_length
        self.grid = [[Empty(config, x_pos, y_pos) for x_pos in range(self.width)] for y_pos in range(self.height)]

        # testing, change later
        i = 0
        while i < 15:
            y = randint(0, config.column_length - 1)
            x = randint(0, config.row_length - 1)
            if self.grid[y][x].content == "empty":
                self.grid[y][x] = Danger(config, x, y)
                i += 1
        i = 0
        while i < 30:
            y = randint(0, config.column_length - 1)
            x = randint(0, config.row_length - 1)
            if self.grid[y][x].content == "empty":
                self.grid[y][x] = Food(config, x, y)
                i += 1
        #testing, change later
    
    def draw(self, config, display):
        for column in self.grid:
            for tile in column:
                tile.draw(config, display)
    
    def spread(self, config):
        for column in self.grid:
            for tile in column:
                if tile.content == "danger":
                    tile.spread(self.grid, config)
