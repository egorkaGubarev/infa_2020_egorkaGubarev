"""
Модуль кнопки
"""

from pygame.draw import *


class Button:
    """
    Описывает кнопку
    """

    def __init__(self, click_handler, color: tuple, height: int, width: int, x: int, y: int):
        """
        Параметры кнопки

        click_handler - функция, исполняемая при нажатии кнопки
        color -  цвет
        height - высота в [px]
        width - ширина в [px]

        Экранная система координат:
        Начало - верхний левый угол экрана
        Ось x горизонтально вправао
        Ось y вертикально вниз

        x - экранная координата x верхнего левого края кнопки в [px]
        y - экранная координата y верхнего левого края кнопки в [px]
        """

        self.click_handler = click_handler
        self.color: tuple = color
        self.height: int = height
        self.width: int = width
        self.x: int = x
        self.y: int = y

    def check_click(self, click_pos: list):
        """
        Проверяет, нажата ли кнопка

        click_pos - позиция нажатия мыши
        """

        height: int = self.height  # Высота кнопки в [px]
        mouse_x: int = click_pos[0]  # Экранная координата x нажатия в [px]
        mouse_y: int = click_pos[1]  # Экранная координата y нажатия в [px]
        width: int = self.width  # Ширина кнопки в [px]
        x: int = self.x  # Экранная координата x верхнего левого угла кнопки в [px]
        y: int = self.y  # Экранная координата y верхнего левого угла кнопки в [px]

        if x <= mouse_x <= x + width and y <= mouse_y <= y + height:
            return True
        else:
            return False

    def draw(self, screen):
        """
        Рисует кнопку на экране

        screen - экран для рисования
        """

        color: tuple = self.color  # Цвет
        height: int = self.height  # Высота кнопки в [px]
        width: int = self.width  # Ширина кнопки в [px]
        x: int = self.x  # Экранная координата x верхнего левого угла кнопки в [px]
        y: int = self.y  # Экранная координата y верхнего левого угла кнопки в [px]

        rect(screen, color, (x, y, width, height))
