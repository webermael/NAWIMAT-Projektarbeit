import pygame

def render_world(world):
    for row in world.grid:
        for field in row:
            print(field.position.y, end="")
        print("\n")
