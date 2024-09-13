from world.tile import Tile
from random import randint
import pygame

class Food(Tile):
  def __init__(self, inputs, x_pos, y_pos):
    Tile.__init__(self, inputs["size"]["tile_width"], x_pos, y_pos, "food")
    self.spread_timer = randint(inputs["food"]["min_spread"], inputs["food"]["max_spread"])

  def draw(self, tile_width, display):
    pygame.draw.rect(display, (0, 255, 0), (self.position.x * tile_width, self.position.y * tile_width, tile_width, tile_width))
  
  def spread(self, inputs, world):
    if self.spread_timer == 0:
      x = randint(0, inputs["size"]["row_length"] - 1)
      y = randint(0, inputs["size"]["column_length"] - 1)
      if world[y][x].content == "empty" and randint(0, inputs["food"]["spread_chance"]) == 0:
        world[y][x] = Food(inputs, x, y)
      self.spread_timer = randint(inputs["food"]["min_spread"], inputs["food"]["max_spread"])
    else:
      self.spread_timer -= 1


class Danger(Tile):
  def __init__(self, inputs, x_pos, y_pos):
    Tile.__init__(self, inputs["size"]["tile_width"], x_pos, y_pos, "danger")
    self.green_value = randint(17, 140)
    self.change = 15
    self.lifetime = randint(inputs["danger"]["min_life"], inputs["danger"]["max_life"])

  def draw(self, tile_width, display):
    if self.green_value <= 16 or self.green_value > 130:
      self.change *= -1
    self.green_value += self.change
    pygame.draw.rect(display, (255, self.green_value, 0), (self.position.x * tile_width, self.position.y * tile_width, tile_width, tile_width))
  
  def spread(self, inputs, world):
    if self.lifetime > 0:
      for y in range(self.position.y - 1, self.position.y + 2):
        for x in range(self.position.x - 1, self.position.x + 2):

          if y >= 0 and y < inputs["size"]["column_length"] and x >= 0 and x < inputs["size"]["row_length"]:
            if randint(0, inputs["danger"]["spread_chance"]) == 0 and world[y][x].content != "danger":
              world[y][x] = Danger(inputs, x, y)

      self.lifetime -= 1
    else:
      world[self.position.y][self.position.x] = Empty(inputs["size"]["tile_width"], self.position.x, self.position.y)


class Empty(Tile):
  def __init__(self, tile_width, x_pos, y_pos):
    Tile.__init__(self, tile_width, x_pos, y_pos, "empty")
    
