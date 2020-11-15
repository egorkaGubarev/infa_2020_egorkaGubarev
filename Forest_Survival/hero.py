"""
Модуль героя
"""

from pygame.draw import *


class Hero(object):
    """
    Описывает героя
    """

    def __init__(self, game, screen):
        """
        Параметры

        Объекты
        game - объект игры

        Графика
        screen - экран pygame
        """

        # Логика
        self.satiety: float = 4186800  # Пищевая энергия в [Дж]
        self.satiety_max: int = 8373600  # Максимальня пищевая нергия в [Дж]
        self.satiety_reduce: int = self.satiety_max // game.day_length  # Скорость голодания в [Дж/с]

        # Объекты
        self.game = game

        # Графика
        self.color: tuple = (128, 0, 0)  # Цвет - красный
        self.radius: int = 5  # Радиус в [px]
        self.screen = screen

    # --- Логика ---
    def get_hungry(self):
        """
        Уменьшает сытость
        """

        # Логика
        satiety: float = self.satiety  # Пищевая энергия в [Дж]
        satiety_reduce: int = self.satiety_reduce  # Скорость голодания в [Дж/c]

        # Объекты
        game = self.game  # Объект игры

        self.satiety: float = satiety - satiety_reduce * game.time_step  # Новая пищевая энергия в [Дж]

    # --- Графика ---
    def draw(self):
        """
        Нарисовать героя
        """

        # Графика
        color: tuple = self.color  # Цвет героя
        radius: int = self.radius  # Радиус героя в [px]
        screen = self.screen  # Экран pygame
        screen_height: int = screen.get_height()  # Высота экрана в [px]
        screen_width: int = screen.get_width()  # Ширина экрана в [px]

        # Физика
        x: int = screen_width // 2  # Координата x героя на экране в [px]
        y: int = screen_height // 2  # Координата y героя на экране в [px]

        circle(screen, color, (x, y), radius)

    # --- Обработка ---
    def log(self):
        """
        Выводит информацию о герое в консоль для отладки
        """

        # Логика
        satiety: float = self.satiety

        print('Satiety:', satiety)
        print('--- Game cycle ---')

    def process(self):
        """
        Обрабатывает события героя
        """

        self.get_hungry()
        self.draw()
        
        # Отладка
        # self.log()
