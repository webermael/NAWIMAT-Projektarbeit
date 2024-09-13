from world.tile import Tile
from world.environment import Danger, Food, Empty
from random import randint

class World:
    def __init__(self, inputs):
        self.width = inputs["size"]["row_length"]
        self.height = inputs["size"]["column_length"]
        self.grid = [["empty" for x_pos in range(self.width)] for y_pos in range(self.height)] 

        i = 0
        while i < inputs["danger"]["count"]:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "danger"
                i += 1
        i = 0
        while i < inputs["food"]["count"]:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "food"
                i += 1

        for row in range(len(self.grid)):
            for tile in range(len(self.grid[0])):
                if self.grid[row][tile] == "food":
                    self.grid[row][tile] = Food(inputs, tile, row)
                elif self.grid[row][tile] == "danger":
                    self.grid[row][tile] = Danger(inputs, tile, row)
                else:
                    self.grid[row][tile] = Empty(inputs["size"]["tile_width"], tile, row)
    
    def draw(self, tile_width, display):
        for column in self.grid:
            for tile in column:
                tile.draw(tile_width, display)
    
    def update(self, inputs):
        for column in self.grid:
            for tile in column:
                tile.spread(inputs, self.grid)
