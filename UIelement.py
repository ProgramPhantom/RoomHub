import pygame


class UIElement(pygame.Surface):
    def __init__(self, wh):
        super.__init__(wh)