import pygame

from pygame.draw import *
from pygame.font import *


class Button:

    def __init__(self, parameter: any, values_list: list, texts_list: list, x: int, y: int):
        """
        Zero point is top left
        x in [px]
        y in [px]
        """

        # Button
        self.color: tuple = (0, 0, 128)
        self.parameter: any = parameter
        self.values: list = values_list
        self.value_index: int = 0
        self.value: any = values_list[self.value_index]
        self.x: int = x
        self.y: int = y

        # Text
        self.font_name: str = 'times.ttf'
        self.font_size: int = 36
        self.smoothing: bool = True
        self.text_color: tuple = (128, 0, 0)
        self.texts: list = texts_list
        self.text_str_index: int = 0
        self.text_str: str = texts_list[self.text_str_index]

    def draw(self, screen):

        # Text
        font = Font(self.font_name, self.font_size)
        texts: list = self.texts
        text_str_index: int = self.text_str_index
        text_str: str = texts[text_str_index]
        smoothing: bool = self.smoothing
        text_color: tuple = self.text_color
        text = font.render(text_str, smoothing, text_color)

        # Button
        color: tuple = self.color
        height: int = self.font_size  # in [px]
        width: int = len(text_str) * self.font_size  # in [px]
        x: int = self.x  # in [px]
        y: int = self.y  # in [px]

        rect(screen, color, (x, y, width, height))
        screen.blit(text, (x, y))

    def process_click(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Button
            height: int = self.font_size  # in [px]
            value_index: int = self.value_index
            values_amount: int = len(self.values)
            width: int = len(self.text_str) * self.font_size  # in [px]
            x: int = self.x  # in [px]
            y: int = self.y  # in [px]

            # Mouse
            mouse_x: int = event.pos[0]  # in [px]
            mouse_y: int = event.pos[1]  # in [px]

            # Text
            texts_str_amount: int = len(self.texts)
            text_str_index: int = self.text_str_index

            if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
                raw_text_str_index: int = text_str_index + 1
                raw_value_index: int = value_index + 1
                self.text_str_index: int = raw_text_str_index % texts_str_amount
                self.value_index: int = raw_value_index % values_amount
                return True
            else:
                return False
