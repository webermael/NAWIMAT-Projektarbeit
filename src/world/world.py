from world.environment import Danger, Food, Empty
from random import randint

class World:
    '''
    generates empty tiles
    places food and danger
    used to update and draw all tiles
    '''
    def __init__(self, inputs):
        self.width = inputs["size"]["row_length"]
        self.height = inputs["size"]["column_length"]
        # creates a full world with "empty" strings
        self.grid = [["empty" for x_pos in range(self.width)] for y_pos in range(self.height)]

        # if more danger tiles are input than there are empty tiles in the world, the danger count is capped 
        if self.width * self.height < inputs["danger"]["count"]:
            danger_count = self.width * self.height
        else:
            danger_count = inputs["danger"]["count"]
        current_danger = 0
        # replaces "empty" strings with danger according to input 
        while current_danger < danger_count:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "danger"
                current_danger += 1
        
        # same as danger placement
        if self.width * self.height - danger_count < inputs["food"]["count"]:
            food_count = self.width * self.height - danger_count
        else:
            food_count = inputs["food"]["count"]
        current_food = 0
        while current_food < food_count:
            y = randint(0, self.height - 1)
            x = randint(0, self.width - 1)
            if self.grid[y][x] == "empty":
                self.grid[y][x] = "food"
                current_food += 1
        
        # replaces all strings with actual tile objects
        for row in range(len(self.grid)):
            for tile in range(len(self.grid[0])):
                if self.grid[row][tile] == "food":
                    self.grid[row][tile] = Food(inputs, tile, row)
                elif self.grid[row][tile] == "danger":
                    self.grid[row][tile] = Danger(inputs, tile, row)
                else:
                    self.grid[row][tile] = Empty(tile, row)
    
    def draw(self, tile_width, display):
        for column in self.grid:
            for tile in column:
                tile.draw(tile_width, display)
    
    def update(self, inputs):
        for column in self.grid:
            for tile in column:
                tile.spread(inputs, self.grid)
