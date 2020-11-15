"""
Главный модуль
"""

import pygame

from game import Game
from hero import Hero
from indicator import Indicator

# Графика
screen_height: int = 700  # Высота экрана в пикселях
screen_width: int = 1200  # Ширина экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Объект экрана pygame

# Объекты
game = Game(screen)  # Объект игры
hero = Hero(game, screen)  # Объект героя
satiety_percent: float = 100 * hero.satiety / hero.satiety_max  # Сытость героя в [%]
indicator_satiety = Indicator('Сытость', screen, satiety_percent, 0, 0)  # Объект индикатора сытости

while game.status != 'finished':  # Пока игра не завершена
    game.update_logic()
    game.update_graphics()
    hero.process()
    satiety_percent: float = 100 * hero.satiety / hero.satiety_max  # Сытость героя в [%]
    indicator_satiety.value = satiety_percent  # Значение индикатора сытости в [%]
    indicator_satiety.process()
