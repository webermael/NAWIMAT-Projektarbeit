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
    self.lifetime = randint(config.danger_min_life, config.danger_max_life)

  def draw(self, config, display):
    pygame.draw.rect(display, (255, 0, 0), (self.position.x * config.tile_width, self.position.y * config.tile_width, config.tile_width, config.tile_width))
  
  
  def spread(self, world, config):
    if self.lifetime > 0:
      for y in range(self.position.y - 1, self.position.y + 2):
        for x in range(self.position.x - 1, self.position.x + 2):
          if y >= 0 and y < config.column_length and x >= 0 and x < config.row_length:
            if randint(0, 100) == 0:
              world[y][x] = Danger(config, x, y)
      self.lifetime -= 1
    else:
      world[self.position.y][self.position.x] = Empty(config, self.position.x, self.position.y)


class Empty(Tile):
  def __init__(self, config, x_pos, y_pos):
    Tile.__init__(self, config, x_pos, y_pos, "empty")
    
