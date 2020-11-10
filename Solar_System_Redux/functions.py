"""
Модуль, содержащий функции
"""

from simulation import *
from user_interface import *


def create_screen(full_screen_needed: bool, height: int, width: int):
    """
    Создаёт экран

    full_screen_needed - флаг полного экрана
    height - высота экрана в [px]
    width - ширина экрана в [px]
    """

    if full_screen_needed:
        screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)  # Создание полного экрана
    else:
        screen = pygame.display.set_mode(width, height)  # Создание полного экрана в окне
    return screen


def create_simulation(clock, colors_dict: dict, fps: int, screen, user_interface):
    """
    Создаёт симуляцию

    clock - часы
    colors_dict - словарь цветов
    fps - частота обновления экрана в [Гц]
    screen - экран для рисования
    user_interface - объект пользовательского интерфейса
    """

    simulation = Simulation(clock, colors_dict, fps, screen, user_interface)  # Создание симуляции
    return simulation


def create_user_interface(clock, colors_dict: dict, fps: int, screen):
    """
    Создаёт пользовательский интерфейс

    clock - часы
    colors_dict - словарь цветов
    fps - частота обновления экрана в [Гц]
    screen - экран для рисования
    """

    user_interface = UserInterface(clock, colors_dict, fps, screen)
    return user_interface
