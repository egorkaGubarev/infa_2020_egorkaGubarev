import pygame

from pygame.draw import *
from pygame.font import *


class Button:

    def __init__(self, parameter: any, text_str: any, values_list: list, x: int, y: int):
        """
        width in [px]
        Zero point is top left
        x in [px]
        y in [px]
        """

        # Button
        self.color: tuple = (0, 0, 128)
        self.parameter: any = parameter
        self.width: int = 190  # in [px]
        self.x: int = x
        self.y: int = y

        # Text
        self.font_name: str = 'times.ttf'
        self.font_size: int = 36
        self.smoothing: bool = True
        self.text_color: tuple = (128, 0, 0)
        self.text_str: str = text_str

        # Value
        self.value_index: int = 0
        self.values_list: list = values_list
        self.value: any = self.values_list[self.value_index]

    def draw(self, screen):

        # Text
        font = Font(self.font_name, self.font_size)
        text_str: str = self.text_str
        smoothing: bool = self.smoothing
        text_color: tuple = self.text_color
        text = font.render(text_str, smoothing, text_color)

        # Button
        color: tuple = self.color
        height: int = self.font_size  # in [px]
        width: int = self.width  # in [px]
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        rect(screen, color, (x, y, width, height))
        screen.blit(text, (x, y))

    def process_click(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Button
            height: int = self.font_size  # in [px]
            width: int = self.width  # in [px]
            x: int = self.x  # in [px]
            y: int = self.y  # in [px]

            # Mouse
            mouse_x: int = event.pos[0]  # in [px]
            mouse_y: int = event.pos[1]  # in [px]

            # Value
            value_index: int = self.value_index
            values_list: list = self.values_list
            values_amount: int = len(values_list)

            if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                raw_value_index: int = value_index + 1
                self.value_index: int = raw_value_index % values_amount
                self.value: any = values_list[value_index]
                return True
            else:
                return False
