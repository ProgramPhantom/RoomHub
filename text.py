import pygame
import posMananger


class Text:
    def __init__(self, parent, name, content, font, type, font_colour, size, x, y):
        self.parent = parent  # Parent surface object

        self.content = content
        self.font_colour = font_colour
        self.font_size = size
        self.type = type

        if type == "sys":
            self.font = pygame.font.SysFont(font, size)
        else:
            self.font = pygame.font.Font("fonts/" + font, self.font_size)

        self.text = self.font.render(content, 1, font_colour)
        self.name = name

        self.rect = self.text.get_rect()

        if x == "centre":
            self.x = posMananger.center_x(parent.get_width(), self.rect.width)
        else:
            self.x = x

        if y == "centre":
            self.y = posMananger.center_y(parent.get_height(), self.rect.height)
        else:
            self.y = y

    def draw(self):
        self.parent.blit(self.text, (self.x, self.y))

    def update_text(self, content="default", font_colour="default"):
        """
        Change the text content and colour of the text
        """
        if content == "default": content = self.content
        if font_colour == "default": font_colour = self.font_colour

        self.text = self.font.render(content, 1, font_colour)
        self.rect = self.text.get_rect()

    def change_font(self, font="default", size="default"):
        """
        Change the font type and size
        """
        if font == "default": font = self.font
        if size == "default": size = self.font_size
        self.font = pygame.font.SysFont(font, size)

# t = Text(win, "Peen", "arial", (0, 0, 0), 40, 20, 20)
