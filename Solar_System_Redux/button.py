"""
Модуль кнопки
"""

from pygame.draw import *

from settings import button_color


class Button:
    """
    Описывает кнопку
    """

    def __init__(self, height: int, screen, width: int, x: int, y: int):
        """
        Параметры кнопки

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

        self.color: tuple = button_color
        self.height = height
        self.width = width
        self.screen = screen
        self.x: int = x
        self.y: int = y

    def check_click(self, click_pos: list):
        """
        Проверяет, нажата ли кнопка

        click_pos - позиция нажатия мыши
        """

        x = click_pos[0]  # Экранная координата x нажатия в [px]
        y = click_pos[1]  # Экранная координата y нажатия в [px]
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False

    def draw(self):
        """
        Рисует кнопку на экране
        """

        rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    @staticmethod
    def process_click(simulation):
        """
        Обрабатывает нажатие на кнопку

        simulation - статус симуляции
        """

        if simulation.dt > 0:
            simulation.dt = 0  # Пауза
        else:
            simulation.dt = 1 / simulation.fps * 500000  # Возобновление симуляции
