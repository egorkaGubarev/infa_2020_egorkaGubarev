"""
Модуль героя
"""

from pygame.draw import *


class Hero(object):
    """
    Описывает героя
    """

    def __init__(self, screen):
        """
        Параметры

        Графика
        screen - экран pygame
        """

        # Графика
        self.color: tuple = (128, 0, 0)  # Цвет - красный
        self.radius: int = 5  # Радиус в [px]
        self.screen = screen

    # --- Графика ---
    def draw(self):
        """
        Нарисовать героя
        """

        # Графика
        color: tuple = self.color  # Цвет героя
        radius: int = self.radius  # Радиус героя в [px]
        screen = self.screen  # Экран pygame
        screen_height: int = screen.get_window_size()[0]  # Высота экрана в [px]
        screen_width: int = screen.get_window_size()[1]  # Ширина экрана в [px]

        # Физика
        x: int = screen_width // 2  # Координата x героя на экране в [px]
        y: int = screen_height // 2  # Координата y героя на экране в [px]

        circle(screen, color, (x, y), radius)
