from world.tile import Tile

class World:
    def __init__(self, config):
        self.width = config.row_length
        self.height = config.column_length
        self.grid = [[Tile(config, row, column) for column in range(self.width)] for row in range(self.height)]
