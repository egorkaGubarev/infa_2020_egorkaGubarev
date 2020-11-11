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
        self.text_color: tuple = (128, 0, 0)
        self.text_str: str = text
        self.x: int = x
        self.y: int = y

    def process_click(self, event):

        height: int = self.font_size  # in [px]
        mouse_x: int = event.pos[0]  # in [px]
        mouse_y: int = event.pos[1]  # in [px]
        width: int = len(self.text_str) * self.font_size  # in [px]
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
            return True
        else:
            return False

    def draw(self, screen):

        color: tuple = self.color
        font = Font(self.font_name, self.font_size)
        text_str: str = self.text_str
        height: int = self.font_size  # in [px]
        smoothing: bool = self.smoothing
        text_color: tuple = self.text_color
        text = font.render(text_str, smoothing, text_color)
        width: int = len(text_str) * self.font_size  # in [px]
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        rect(screen, color, (x, y, width, height))
        screen.blit(text, (x, y))
