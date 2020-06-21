import pygame
import posMananger


class Text:
    def __init__(self, parent, content, font, font_colour, size, x, y):
        self.parent = parent  # Parent surface object

        self.content = content
        self.font_colour = font_colour
        self.font_size = size

        self.font = pygame.font.SysFont(font, size)
        self.text = self.font.render(content, 1, font_colour)

        if x == "center":
            posMananger.center_x()
        else:
            self.x = x

        if y == "center":
            posMananger.center_y()
        else:
            self.y = y

        self.rect = self.text.get_rect()

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
