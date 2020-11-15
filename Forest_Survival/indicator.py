"""
Модуль индикаторов
"""

import pygame

from pygame.draw import *
from pygame.font import *

pygame.font.init()


class Indicator(object):
    """
    Описывает индикатор
    """

    def __init__(self, name, screen, value: float, x: int, y: int):
        """
        Параметры
        Отсчёт координат от левого верхнего угла индикатора

        Логика
        value - значение индицируемой величины в [%]

        Графика
        screen - экран pygame
        x - координата x индикатора в [px]
        y - координата y индикатора в [px]

        Текст
        name - название индикатора
        """

        # Логика
        self.value: float = value

        # Графика
        self.color_active: tuple = (27, 60, 24)  # Цвет активной части
        self.color_passive: tuple = (0, 0, 0)  # Цвет пассивной части - чёрный
        self.height: int = 36  # Высота индикатора в [px]
        self.width_full: int = 100  # Полная длина индикатора в [px]
        self.x: int = x
        self.y: int = y
        self.screen = screen

        # Текст
        self.font_name = None  # Название шрифта
        self.font_smoothing: bool = True  # Сглаживание шрифта
        self.name: str = name
        self.text_space: int = 10  # Ширина пробела между индикатором и его названием

    # --- Графика ---
    def draw(self):
        """
        Рисует индикатор
        Координаты названия отсчитываются от его левого верхнего угла
        """

        # Логика
        value: float = self.value  # Значение индицируемой величины в [%]

        # Графика
        color_active: tuple = self.color_active  # Цвет активной части
        color_passive: tuple = self.color_passive  # Цвет пассивой части
        height: int = self.height  # Высота индикатора в [px]
        width_full: int = self.width_full  # Полная длина индикатора в [px]
        width_active: float = width_full * value // 100  # Длина активной части в [px]
        width_active_int: int = round(width_active)  # Округлённая длина активной части в [px]
        x: int = self.x  # Координата x индикатора в [px]
        y: int = self.y  # Координата y индикатора в [px]
        screen = self.screen  # Экран pygame

        # Текст
        font_color: tuple = self.color_active  # Цвет шрифта
        font_name = self.font_name  # Название шрифта
        font_size: int = self.height  # Размер шрифта
        font_smoothing: bool = self.font_smoothing
        font = Font(font_name, font_size)  # Шрифт pygame
        name: str = self.name  # Название индикатора
        text = font.render(name, font_smoothing, font_color)
        text_space: int = self.text_space  # Ширина пробела между индикатором и его названием
        text_x: int = x + width_full + text_space  # Координата x названия в [px]

        rect(screen, color_passive, (x, y, width_full, height))
        rect(screen, color_active, (x, y, width_active_int, height))
        screen.blit(text, (text_x, y))

    # --- Обработка ---
    def log(self):
        """
        Выводит данные в консоль для отладки
        """

        # Графика
        width_full: int = self.width_full  # Полная длина индикатора в [px]

        print('Width active int:', width_full)
        print('--- Game cycle ---')

    def process(self):
        """
        Обрабатывает события индикатора
        """

        self.draw()

        # Отладка
        # self.log()
