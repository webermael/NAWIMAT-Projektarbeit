class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, config, x_pos, y_pos, content):
        self.width = config.tile_width
        self.height = config.tile_height
        self.position = Position(x_pos, y_pos)
        self.content = content
        self.has_organism = False
    
    def draw(self, config, display):
        pass
    
    def spread(self, world, config):
        pass

