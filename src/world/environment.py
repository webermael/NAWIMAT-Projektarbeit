from tile import Tile

class Food(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "food")

class Danger(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "danger")

class Empty(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "empty")
    
