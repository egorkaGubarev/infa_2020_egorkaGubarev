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

        Координаты центров объектов

        game - объект игры
        screen - экран pygame
        """

        # Физика
        self.speed_max: float = 2  # Максимальная скорость героя в [м/с]
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
    @staticmethod
    def calculate_speed_reduce(directions_list: list):
        """
        Вычисляет фактор уменьшения скорости

        directions_list - список направлений, по которым сейчас движется герой
        """

        directions_count: int = len(directions_list)  # Количество направлений, по которым сейчас идёт герой
        if directions_count == 2:  # Если герой идёт сразу по 2 направлениям
            speed_reduce: float = math.sqrt(2)  # Сохранение полной скорости героя
        else:
            speed_reduce: float = 1  # Сохранение полной скорости героя
        return speed_reduce

    def check_live_parameters(self):
        """
        Проверяет жизненно важные параметры героя
        """

        if self.satiety == 0:  # Если герой смертельно голоден
            self.get_dead()
        else:
            self.status: str = 'alive'  # Герой жив

    def get_dead(self):
        """
        Убивает героя
        """

        self.status: str = 'dead'  # Герой мёртв
        self.game.finish()

    def get_hungry(self):
        """
        Уменьшает сытость
        """

        delta_satiety: float = self.satiety_reduce * self.game.time_step  # Квант голодания в [Дж]
        new_satiety: float = self.satiety - delta_satiety  # Новая пищевая энергия в [Дж]
        new_satiety_int: int = round(new_satiety)  # Округлённое значение новой пищевой энергии в [Дж]
        self.satiety = max(0, new_satiety_int)  # Пищевая энергия не может быть отрицательной

    def move(self, direction: str, speed: float):
        """
        Перемещает героя

        direction - направление перемещения
        speed - скорость героя
        """

        delta_distance: float = speed * self.game.time_step  # Квант перемещения в [м]

        if direction == 'up':  # Если герой идёт вверх
            self.y -= delta_distance  # Координата y героя в [м]
        if direction == 'left':  # Если герой идёт влево
            self.x -= delta_distance  # Координата x героя в [м]
        if direction == 'down':  # Если герой идёт вниз
            self.y += delta_distance  # Координата y героя в [м]
        if direction == 'right':  # Если герой идёт вправо
            self.x += delta_distance  # Координата x героя в [м]

    def process_keys_motion(self):
        """
        Обрабатывает информацию о нажатых клавишах перемещения
        """

        directions_dict: dict = {pygame.K_w: 'up',  # Словарь направлений
                                 pygame.K_a: 'left',
                                 pygame.K_s: 'down',
                                 pygame.K_d: 'right'}
        directions_list: list = []  # Список направлений, по которым сейчас идёт герой
        keys_pressed: list = pygame.key.get_pressed()  # Список нажатых клавиш
        for key in directions_dict:
            if keys_pressed[key] == 1:  # Если нажата клавиша перемещения
                directions_list.append(directions_dict[key])
        speed_reduce: float = self.calculate_speed_reduce(directions_list)  # Фактор уменьшения скорости
        actual_speed: float = self.speed_max / speed_reduce  # Действительая скорость героя в [м/с]

        for direction in directions_list:
            self.move(direction, actual_speed)

    # --- Графика ---
    def draw(self):
        """
        Нарисовать героя
        """

        x: int = self.screen.get_width() // 2  # Координата x героя на экране в [px]
        y: int = self.screen.get_height() // 2  # Координата y героя на экране в [px]

        circle(self.screen, self.color, (x, y), self.radius)

    # --- Обработка ---
    def log(self):
        """
        Выводит информацию о герое в консоль для отладки
        """

        print('Y:', self.y)
        print('--- Game cycle ---')

    def process(self):
        """
        Обрабатывает события героя
        """

        self.get_hungry()
        self.check_live_parameters()
        self.process_keys_motion()
        self.draw()

        # Отладка
        # self.log()
