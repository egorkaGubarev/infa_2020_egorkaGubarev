"""
Модуль кнопки
"""

from pygame.draw import *


class Button:
    """
    Описывает кнопку
    """

    def __init__(self, colors_dict: dict, height: int, screen, width: int, x: int, y: int):
        """
        Параметры кнопки

        color_dict - словарь цветов
        height - высота в [px]
        screen - экран для рисования
        width - ширина в [px]

        Экранная система координат:
        Начало - верхний левый угол экрана
        Ось x горизонтально вправао
        Ось y вертикально вниз

        x - экранная координата x верхнего левого края кнопки в [px]
        y - экранная координата y верхнего левого края кнопки в [px]
        """

        self.colors_dict: dict = colors_dict  # FIXME кнопка должна принимать конкретный цвет
        self.height: int = height
        self.screen = screen
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

    def draw(self):
        """
        Рисует кнопку на экране
        """

        colors_dict = self.colors_dict  # Словарь цветов
        color: tuple = colors_dict['dark_blue']  # Тёмно-синий цвет
        height: int = self.height  # Высота кнопки в [px]
        screen = self.screen  # Экран для рисования
        width: int = self.width  # Ширина кнопки в [px]
        x: int = self.x  # Экранная координата x верхнего левого угла кнопки в [px]
        y: int = self.y  # Экранная координата y верхнего левого угла кнопки в [px]

        rect(screen, color, (x, y, width, height))

    @staticmethod
    def process_click(simulation):  # FIXME необходим общий случай
        """
        Обрабатывает нажатие на кнопку

        simulation - объект Симуляция
        """

        if simulation.dt > 0:
            simulation.dt = 0  # Пауза
        else:
            simulation.dt = 1 / simulation.fps * 500000  # Возобновление симуляции
