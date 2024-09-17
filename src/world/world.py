from world.tile import Tile
from world.environment import Danger, Food, Empty
from random import randint

class World:
    def __init__(self, inputs):
        self.width = inputs["size"]["row_length"]
        self.height = inputs["size"]["column_length"]
        self.grid = [["empty" for x_pos in range(self.width)] for y_pos in range(self.height)] # creates a full world with "empty" strings

        # if more danger tiles are input than there are tiles in the world, the danger count is capped 
        if self.width * self.height < inputs["danger"]["count"]:
            danger_count = self.width * self.height
        else:
            danger_count = inputs["danger"]["count"]
        current_danger = 0
        # replaces as many empty strings with danger as the input says
        while current_danger < danger_count:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "danger"
                current_danger += 1
        
        # if more food tiles are input than there are empty tiles in the world, the food count is capped
        if self.width * self.height - danger_count < inputs["food"]["count"]:
            food_count = self.width * self.height - danger_count
        else:
            food_count = inputs["food"]["count"]
        # replaces as many empty strings with danger as the input says
        current_food = 0
        while current_food < food_count:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "food"
                current_food += 1
        
        # replaces all strings with actual tile objects, doing the first step with strings saves some time
        for row in range(len(self.grid)):
            for tile in range(len(self.grid[0])):
                if self.grid[row][tile] == "food":
                    self.grid[row][tile] = Food(inputs, tile, row)
                elif self.grid[row][tile] == "danger":
                    self.grid[row][tile] = Danger(inputs, tile, row)
                else:
                    self.grid[row][tile] = Empty(tile, row)
    
    # draws all tiles
    def draw(self, tile_width, display):
        for column in self.grid:
            for tile in column:
                tile.draw(tile_width, display)
    
    # updates/spreads all tiles
    def update(self, inputs):
        for column in self.grid:
            for tile in column:
                tile.spread(inputs, self.grid)
