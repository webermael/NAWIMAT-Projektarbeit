from world.tile import Tile
from random import randint, random
import pygame


class Food(Tile):
  def __init__(self, inputs, x_pos, y_pos):
    Tile.__init__(self, x_pos, y_pos, "food")
    self.spread_timer = randint(inputs["food"]["min_spread"], inputs["food"]["max_spread"])

  # draws a green square
  def draw(self, tile_width, display):
    pygame.draw.rect(display, (0, 255, 0), (self.position.x * tile_width, self.position.y * tile_width, tile_width, tile_width))
  
  # turns a random empty tile into food
  def spread(self, inputs, world):
    if self.spread_timer == 0:
      x = randint(0, inputs["size"]["row_length"] - 1)
      y = randint(0, inputs["size"]["column_length"] - 1)
      if world[y][x].content == "empty":
        world[y][x] = Food(inputs, x, y)
      # sets a random timer for when the next food will be spread
      self.spread_timer = randint(inputs["food"]["min_spread"], inputs["food"]["max_spread"])
    else:
      self.spread_timer -= 1


class Danger(Tile):
  def __init__(self, inputs, x_pos, y_pos):
    Tile.__init__(self, x_pos, y_pos, "danger")
    self.green_value = randint(17, 140)
    self.green_change = 15
    self.lifetime = randint(inputs["danger"]["min_life"], inputs["danger"]["max_life"])

  # draws a red square
  # green color value grows and shrinks over time, turning it more orange and back to red
  def draw(self, tile_width, display):
    if self.green_value <= 16 or self.green_value > 130:
      self.green_change *= -1
    self.green_value += self.green_change
    pygame.draw.rect(display, (255, self.green_value, 0), (self.position.x * tile_width, self.position.y * tile_width, tile_width, tile_width))
  
  # turns adjacent tiles into fire
  def spread(self, inputs, world):
    if self.lifetime > 0:
      # with a given chance, turns a random tile around itself into fire, if it isn't already
      if random() <= inputs["danger"]["spread_chance"]:
          y = randint(self.position.y - 1, self.position.y + 1)
          x = randint(self.position.x - 1, self.position.x + 1)
          if y >= 0 and y < inputs["size"]["column_length"] and x >= 0 and x < inputs["size"]["row_length"]:
            if world[y][x].content != "danger":
              world[y][x] = Danger(inputs, x, y)
      self.lifetime -= 1
    # turns into an empty tile when lifetime is zero
    else:
      world[self.position.y][self.position.x] = Empty(self.position.x, self.position.y)


class Empty(Tile):
  def __init__(self, x_pos, y_pos):
    Tile.__init__(self, x_pos, y_pos, "empty")
    
