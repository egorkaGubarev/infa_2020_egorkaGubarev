"""
Модуль леса
"""

import math

from pygame.draw import *
from random import *

from apple import Apple


class Forest(object):
    """
    Описывает лес
    """

    def __init__(self, hero_x: float, hero_y: float, screen):
        """
        Параметры

        Физика
        Координаты героя отсчитываются от его центра
        Словарь прямой состоит из координаты, которую имеет прямая, и её значения
        hero_x - Координата x героя в [м]
        hero_y - Координата y героя в [м]

        Графика
        screen - экран pygame
        """

        # Логика
        self.apples_list: list = []  # Список яблок
        self.scale: int = 35  # Масштаб в [px/м]

        # Физика
        self.down_border_dict: dict = {'coordinate': 'y',
                                       'value': 10}  # Словарь нижней границы леса
        self.hero_x: float = hero_x
        self.hero_y: float = hero_y
        self.left_border_dict: dict = {'coordinate': 'x',
                                       'value': -10}  # Словаь левой границы леса
        self.right_border_dict: dict = {'coordinate': 'x',
                                        'value': 10}  # Словарь правой границы леса
        self.up_border_dict: dict = {'coordinate': 'y',
                                     'value': -10}  # Словарь верхней границы леса
        self.borders_list: list = [self.down_border_dict, self.left_border_dict, self.right_border_dict,
                                   self.up_border_dict]

        # Графика
        self.border_color: tuple = (185, 250, 250)  # Цвет границ
        self.border_width: int = 1  # Толщина границ в [px]
        self.color: tuple = (193, 86, 217)  # Цвет леса
        self.screen = screen

    # --- Логика ---
    def setup(self):
        """
        Действия при создании леса
        """

        self.generate_apples()

    # --- Физика ---
    def calculate_distance_to_line(self, line_dict: dict):
        """
        Вычисляет расстояние от героя до прямой

        Физика
        line_dict - словарь прямой
        """

        if line_dict['coordinate'] == 'x':  # Если необходимо посчитать расстояние вдоль x
            hero_coordinate: float = self.hero_x  # Координата x героя в [м]
        elif line_dict['coordinate'] == 'y':  # Если необходимо посчитать расстояние вдоль y
            hero_coordinate: float = self.hero_y  # Координата y героя в [м]
        else:
            return None
        distance: float = line_dict['value'] - hero_coordinate  # Расстояние от героя до прямой в [м]
        return distance

    def calculate_distance_to_point(self, x: float, y: float):
        """
        Вычисляет расстояние от героя до точки

        Физика
        x - Координата x точки в [м]
        y - Координата y точки в [м]
        """

        hero_x: float = self.hero_x  # Координата x героя в [м]
        hero_y: float = self.hero_y  # Координата y героя в [м]
        x_distance: float = x - hero_x  # Расстояние от героя до точки вдоль оси x в [м]
        y_distance: float = y - hero_y  # Расстояние от героя до точки вдоль оси y в [м]
        distance_list: list = [x_distance, y_distance]  # Компоненты расстояния от героя до точки в [м]
        return distance_list

    def check_border_distance(self, border_dict: dict):
        """
        Проверяет расстояни от игрока до границы

        Физика
        border_dict - словарь границы
        """

        border_distance: float = self.calculate_distance_to_line(border_dict)
        return border_distance

    # --- Объекты ---
    def generate_apples(self):
        """
        Создаёт яблоки
        """

        # Физика
        down_border_dict: dict = self.down_border_dict  # Словарь нижней границы
        left_border_dict: dict = self.left_border_dict  # Словарь левой границы
        right_border_dict: dict = self.right_border_dict  # Словарь правой границы
        up_border_dict: dict = self.up_border_dict  # Словарь верхней границы
        x_left: float = left_border_dict['value']  # Координата x левой границы в [м]
        x_right: float = right_border_dict['value']  # Координата x правой границы в [м]
        x_distance: float = x_right - x_left  # Расстояние между границами вдоль оси x в [м]
        y_down: float = down_border_dict['value']  # Координата y нижней границы в [м]
        y_up: float = up_border_dict['value']  # Координата y верхней границы в [м]
        y_distance: float = y_down - y_up  # Расстояние между границами по y в [м]

        apples_amount: int = 5  # Количество яблок
        for apple_number in range(apples_amount):
            x_apple: float = random() * x_distance + x_left  # Координата x яблока в [м]
            y_apple: float = random() * y_distance + y_up  # Координата y яблока в [м]
            apple = Apple(x_apple, y_apple)  # Объект яблока
            self.apples_list.append(apple)

    # --- Графика ---
    def draw_background(self):
        """
        Рисует фон леса
        """

        # Графика
        color: tuple = self.color  # Цвет леса
        screen = self.screen  # Экран pygame

        screen.fill(color)

    def draw_line(self, coordinate: str, line_distance: float):
        """
        Рисует прямую

        Физика
        coordinate - Координата, вдоль которой рисовать прямую
        line_distance - Расстояние от героя до прямой в [м]
        """

        # Логика
        scale: int = self.scale  # Масшаб в [px/м]

        # Графика
        line_color: tuple = self.border_color  # Цвет линии
        line_width: int = self.border_width  # Толщина линии в [px]
        screen = self.screen  # Экран pygame
        screen_height: int = screen.get_height()  # Высота экрана в [px]
        screen_width: int = screen.get_width()  # Ширина экрана в [px]

        if coordinate == 'x':  # Если нужно отрисовать вертикальную границу
            line_x_raw: float = line_distance * scale  # Расстояние от героя до прямой в [px]
            line_x: int = round(line_x_raw)  # Округлённое расстояние от героя до прямой в [px]
            line_x_cooked: int = line_x + screen_width // 2  # Координата x прямой в [px]
            line_y_1: int = -1  # Верхняя точка выше экрана
            line_y_2: int = screen_height + 1  # Нижняя точка ниже экрана

            line(screen, line_color, [line_x_cooked, line_y_1], [line_x_cooked, line_y_2], line_width)

        elif coordinate == 'y':  # Если нужно отрисовать горизонтальную границу
            line_x_1: int = -1  # Левая точка левее экрана
            line_x_2: int = screen_width + 1  # Правая точка правее экрана
            line_y_raw: float = line_distance * scale  # Расстояние от героя до прямой в [px]
            line_y: int = round(line_y_raw)  # Округлённое расстояние от героя до прямой в [px]
            line_y_cooked: int = line_y + screen_height // 2  # Координата y прямой в [px]

            line(screen, line_color, [line_x_1, line_y_cooked], [line_x_2, line_y_cooked], line_width)

    def draw_object(self, item, item_distance_x: float, item_distance_y: float):
        """
        Рисует объект

        item - объект, который нужно нарисовать
        item_distance_x - Расстояние от героя до точки вдоль оси x в [м]
        item_distance_y - Расстояние от героя до точки вдоль оси y в [м]
        """

        # Логика
        scale: int = self.scale  # Масшаб в [px/м]

        # Графика
        color: tuple = item.color  # Цвет объекта
        radius: int = item.radius  # Радиус объекта в [px]
        screen = self.screen  # Экран pygame
        screen_height: int = screen.get_height()  # Высота экрана в [px]
        screen_width: int = screen.get_width()  # Ширина экрана в [px]

        x_raw: float = item_distance_x * scale  # Расстояние от героя до точки вдоль оси x в [px]
        item_x: int = round(x_raw)  # Округлённое расстояние от героя до точки вдоль оси x в [px]
        item_x_cooked: int = item_x + screen_width // 2  # Координата x точки в [px]
        y_raw: float = item_distance_y * scale  # Расстояние от героя до точки вдоль оси y в [px]
        item_y: int = round(y_raw)  # Округлённое расстояние от героя до точки вдоль оси y в [px]
        item_y_cooked: int = item_y + screen_height // 2  # Координата y точки в [px]

        circle(screen, color, (item_x_cooked, item_y_cooked), radius)

    # --- Обработка ---
    def process(self):
        """
        Обрабатывает события леса
        """

        # Графика
        screen = self.screen  # Экран pygame
        screen_height: int = screen.get_height()  # Высота экрана в [px]
        screen_width: int = screen.get_width()  # Ширина экрана в [px]

        # Максимальное расстояние от героя то точки экрана
        max_distance: float = math.sqrt(screen_height ** 2 + screen_width ** 2)

        # Логика
        apples_list: list = self.apples_list  # Список яблок
        scale: int = self.scale  # Масштаб в [px/м]
        max_draw_distance_raw: float = max_distance // scale  # Максимальное расстояние прорисовки объекта в [м]

        # Дистанция, в пределах которой объекты отрисовываются в [м]
        max_draw_distance: int = math.ceil(max_draw_distance_raw)

        # Физика
        borders_list: list = self.borders_list  # Список границ

        self.draw_background()
        for border_dict in borders_list:
            border_distance: float = self.calculate_distance_to_line(border_dict)  # Расстояние до границы в [м]

            # Если расстяние до границы не превышает расстояния прорисовки
            if abs(border_distance) <= max_draw_distance:
                coordinate: str = border_dict['coordinate']  # Координата, вдоль которой рисовать прямую
                self.draw_line(coordinate, border_distance)
        for apple in apples_list:
            x_apple: float = apple.x  # Координата x яблока в [м]
            y_apple: float = apple.y  # Координата y яблока в [м]
            apple_distance_list: list = self.calculate_distance_to_point(x_apple, y_apple)
            apple_distance_x: float = apple_distance_list[0]  # Расстояние от героя до точки вдоль оси x в [м]
            apple_distance_y: float = apple_distance_list[1]  # Расстояние от героя до точки вдоль оси y в [м]

            # Расстояние от героя до яблока в [м]
            apple_distance: float = math.sqrt(apple_distance_x ** 2 + apple_distance_y ** 2)

            # Если расстяние до яблока не превышает расстояния прорисовки
            if abs(apple_distance) <= max_draw_distance:
                self.draw_object(apple, apple_distance_x, apple_distance_y)
