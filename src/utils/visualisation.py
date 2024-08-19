import pygame

def screen_init(config):
    size = (config.tile_width * config.row_length, config.tile_width * config.column_length)
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    return screen

def screen_update():
    pygame.display.flip()
    # ...

# prints a value for every tile in the world
def render_world(world):
    for row in world.grid:
        for field in row:
            print(field.position.y, end="")
        print("\n")
