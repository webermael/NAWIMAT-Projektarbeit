class Position:
    '''
    position class used by other objects, so you can use x/y coordinates
    '''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Tile:
    '''
    smallest unit of a world
    base class for sub class tiles, since every tile has a position and content
    '''
    def __init__(self, x_pos, y_pos, content):
        self.position = Position(x_pos, y_pos)
        self.content = content
        self.has_organism = False
    
    def draw(self, tile_width, display):
        pass
    
    def spread(self, inputs, world):
        pass

