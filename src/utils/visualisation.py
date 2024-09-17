import pygame

# creates a screen with given size and changes title
def screen_init(inputs):
    size = (inputs["tile_width"] * inputs["row_length"], inputs["tile_width"] * inputs["column_length"])
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("Evolvator")
    return screen


def screen_update():
    pygame.display.flip()
    # ...
