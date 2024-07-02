class Tile:
    def __init__(self, config, row, column):
        self.width = config.tile_width
        self.height = config.tile_height
        self.position = (row, column)
        #self.content = ...

