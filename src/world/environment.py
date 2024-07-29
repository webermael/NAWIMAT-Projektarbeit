from world.tile import Tile
from random import randint
import pygame

class Food(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "food")
  
  def draw(self, config, display):
    pygame.draw.rect(display, (0, 255, 0), (self.position.x * config.tile_width, self.position.y * config.tile_width, config.tile_width, config.tile_width))


class Danger(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "danger")

  def draw(self, config, display):
    pygame.draw.rect(display, (255, 0, 0), (self.position.x * config.tile_width, self.position.y * config.tile_width, config.tile_width, config.tile_width))
  
  
  def spread(self, world, config):
    for i in range(self.position.y - 1, self.position.y + 2):
      for j in range(self.position.x - 1, self.position.x + 2):
        if i >= 0 and i < config.column_length and j >= 0 and j < config.row_length:
          if randint(0, 100) == 0:
            world[i][j] = Danger(config, j, i)


class Empty(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "empty")
    
