from pygame.font import *


class Text:

    def __init__(self, text_str: str, x: int, y: int):
        """
        Zero point is top left
        x in [px]
        y in [px]
        """

        self.color: tuple = (128, 0, 0)
        self.font_name: str = 'times.ttf'
        self.font_size: int = 36
        self.smoothing: bool = True
        self.text_str: str = text_str
        self.x: int = x
        self.y: int = y

    def draw(self, screen):

        font = Font(self.font_name, self.font_size)
        text_str: str = self.text_str
        smoothing: bool = self.smoothing
        color: tuple = self.color
        text = font.render(text_str, smoothing, color)
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        screen.blit(text, (x, y))
