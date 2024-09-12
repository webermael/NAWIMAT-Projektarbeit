from world.tile import Tile
from world.environment import Danger, Food, Empty
from random import randint

class World:
    def __init__(self, inputs):
        self.width = inputs["size"]["row_length"]
        self.height = inputs["size"]["column_length"]
        self.grid = [[Empty(inputs["size"]["tile_width"], x_pos, y_pos) for x_pos in range(self.width)] for y_pos in range(self.height)]

        i = 0
        while i < inputs["danger"]["count"]:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x].content == "empty":
                self.grid[y][x] = Danger(inputs, x, y)
                i += 1
        i = 0
        while i < inputs["food"]["count"]:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x].content == "empty":
                self.grid[y][x] = Food(inputs, x, y)
                i += 1
    
    def draw(self, tile_width, display):
        for column in self.grid:
            for tile in column:
                tile.draw(tile_width, display)
    
    def update(self, inputs):
        for column in self.grid:
            for tile in column:
                tile.spread(inputs, self.grid)
