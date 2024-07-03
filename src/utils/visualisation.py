import pygame

def screen_init(config):
    pygame.init()
    size = (config.tile_height * config.column_length, config.tile_width * config.row_length)
    screen = pygame.display.set_mode(size)
    return screen


# prints a value for every tile in the world
def render_world(world):
    for row in world.grid:
        for field in row:
            print(field.position.y, end="")
        print("\n")
