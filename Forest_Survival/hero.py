"""
Модуль героя
"""

import math
import pygame

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

        # Физика
        self.speed_max: float = 2  # Максимальная скорость героя в [м/с]
        self.speed_reduce: float = 1  # Во столько раз действительная меньше максимальной
        self.x: float = 0  # Координата x героя в [м]
        self.y: float = 0  # Координата y героя в [м]

        # Логика
        self.satiety: float = 4186800  # Пищевая энергия в [Дж]
        self.satiety_max: int = 8373600  # Максимальня пищевая энергия в [Дж]
        self.satiety_reduce: int = self.satiety_max // game.day_length  # Скорость голодания в [Дж/с]
        self.status: str = 'alive'  # Герой жив

        # Объекты
        self.game = game

        # Графика
        self.color: tuple = (206, 181, 75)  # Цвет героя
        self.radius: int = 5  # Радиус в [px]
        self.screen = screen

    # --- Логика ---
    def check_live_parameters(self):
        """
        Проверяет жизненно важные параметры героя
        """

        # Логика
        satiety: float = self.satiety  # Пищевая энергия в [Дж]

        if satiety == 0:  # Если герой смертельно голоден
            self.get_dead()

    def get_dead(self):
        """
        Убивает героя
        """

        # Объекты
        game = self.game  # Объект игры

        self.status: str = 'dead'  # Герой мёртв
        game.status = 'finished'  # Игра завершена

    def get_hungry(self):
        """
        Уменьшает сытость
        """

        # Логика
        satiety: float = self.satiety  # Пищевая энергия в [Дж]
        satiety_reduce: int = self.satiety_reduce  # Скорость голодания в [Дж/c]

        # Объекты
        game = self.game  # Объект игры

        new_satiety: float = satiety - satiety_reduce * game.time_step  # Новая пищевая энергия в [Дж]
        new_satiety_int: int = round(new_satiety)  # Округлённое значение новой пищевой энергии в [Дж]
        self.satiety = max(0, new_satiety_int)  # Пищевая энергия не может быть отрицательной

    def go(self, direction: str):
        """
        Перемещает героя

        Логика
        direction - направление перемещения
        """

        # Объекты
        game = self.game  # Объект игры

        # Физика
        speed_max: float = self.speed_max  # Максимальная скорость героя в [м/с]
        speed_reduce: float = self.speed_reduce  # Во столько раз действительная скорость меньше максимальной
        speed: float = speed_max / speed_reduce  # Действительная скорость героя в [м/с]
        time_step: float = game.time_step  # Квант времени в [с]
        x: float = self.x  # Координата x героя в [м]
        y: float = self.y  # Координата y героя в [м]

        if direction == 'up':  # Если герой идёт вверх
            self.y: float = y - speed * time_step  # Координата y героя в [м]
        if direction == 'left':  # Если герой идёт влево
            self.x: float = x - speed * time_step  # Координата x героя в [м]
        if direction == 'down':  # Если герой идёт вниз
            self.y: float = y + speed * time_step  # Координата y героя в [м]
        if direction == 'right':  # Если герой идёт вправо
            self.x: float = x + speed * time_step  # Координата x героя в [м]

    def process_keys_pressed(self):
        """
        Обрабатывает информацию о нажатых клавишах
        """

        # Логика
        directions_dict: dict = {pygame.K_w: 'up',  # Словарь направлений
                                 pygame.K_a: 'left',
                                 pygame.K_s: 'down',
                                 pygame.K_d: 'right'}
        directions_list: list = []  # Список направлений, по которым сейчас идёт герой
        keys_pressed: list = pygame.key.get_pressed()  # Список нажатых клавиш

        for key in directions_dict:
            if keys_pressed[key] == 1:  # Если нажата клавиша
                directions_list.append(directions_dict[key])
        directions_count: int = len(directions_list)  # Количество направлений, по которым сейчас идёт герой
        if directions_count == 2:  # Если герой идёт сразу по 2 направлениям
            self.speed_reduce: float = math.sqrt(2)  # Сохранение полной скорости героя
        else:
            self.speed_reduce: float = 1  # Сохранение полной скорости героя
        for direction in directions_list:
            self.go(direction)

    # --- Графика ---
    def draw(self):
        """
        Нарисовать героя
        Отсчёт координат от центра героя
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
        y: float = self.y  # Координата y героя в [м]

        print('Y:', y)
        print('--- Game cycle ---')

    def process(self):
        """
        Обрабатывает события героя
        """

        self.get_hungry()
        self.check_live_parameters()
        self.process_keys_pressed()
        self.draw()

        # Отладка
        # self.log()
