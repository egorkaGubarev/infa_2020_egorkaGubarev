"""
Модуль, содержащий функции
"""

from simulation import *


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


def create_simulation(screen):
    """
    Создаёт симуляцию

    screen - экран для рисования
    """

    simulation = Simulation(screen)  # Создание симуляции
    return simulation
