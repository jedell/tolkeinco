import sys, pygame
pygame.init()

class Marker:
    def __init__(self, image, x, y):
        self.image = image
        self.pos = image.get_rect().move(x, y)