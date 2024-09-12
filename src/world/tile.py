class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Tile:
    def __init__(self, tile_width, x_pos, y_pos, content):
        self.width = tile_width
        self.position = Position(x_pos, y_pos)
        self.content = content
        self.has_organism = False
    
    def draw(self, tile_width, display):
        pass
    
    def spread(self, inputs, world):
        pass

