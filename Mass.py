import pygame
import random

class Mass:
    def __init__(self, rendered, mass_x, mass_y, mass_radius):
        self.mass_x = mass_x
        self.mass_y = mass_y
        self.rendered = rendered
        self.mass_radius = mass_radius

    def draw(self, screen, blue):
        pygame.draw.circle(screen, blue, (self.mass_x, self.mass_y), self.mass_radius)

    def rand_location(self):
        self.mass_x = random.randint(0, 1920)
        self.mass_y = random.randint(0, 1080)
