from world.tile import Tile

class World:
    def __init__(self, config):
        self.width = config.row_length
        self.height = config.column_length
        self.grid = [[Tile(config, x_pos, y_pos) for x_pos in range(self.width)] for y_pos in range(self.height)]
