import pygame
from random import randint


print("Hey Apple!")

class Apple():
    def __init__(self):
        self.rect = pygame.Rect((randint(0, 39) * 20, randint(0, 29) * 20, 20, 20))

    def draw(self, main_display):
        pygame.draw.circle(main_display, 'red', self.rect.center, 10)
