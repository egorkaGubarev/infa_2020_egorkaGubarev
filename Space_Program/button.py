from pygame.draw import *
from pygame.font import *


class Button:

    def __init__(self, text: str, x: int, y: int):
        """
        Zero point is top left
        x in [px]
        y in [px]
        """

        self.color: tuple = (0, 0, 128)
        self.font_name: str = 'times.ttf'
        self.font_size: int = 36
        self.smoothing: bool = True
        self.text_color: tuple = (0, 128, 0)
        self.text_str: str = text
        self.x: int = x
        self.y: int = y

    def draw(self, screen):

        color: tuple = self.color
        font = Font(self.font_name, self.font_size)
        text_str: str = self.text_str
        height: int = self.font_size
        smoothing: bool = self.smoothing
        text_color: tuple = self.text_color
        text = font.render(text_str, smoothing, text_color)
        width: int = len(text_str) * self.font_size
        x: int = self.x
        y: int = self.y

        rect(screen, color, (x, y, width, height))
        screen.blit(text, (x, y))
