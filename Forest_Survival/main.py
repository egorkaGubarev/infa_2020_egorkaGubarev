"""
Главный модуль
"""

import pygame

from forest import Forest
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
hero_x: float = hero.x  # Координата x героя в [м]
hero_y: float = hero.y  # Координата y героя в [м]
forest = Forest(hero_x, hero_y, screen)  # Объект леса
satiety_percent: float = 100 * hero.satiety / hero.satiety_max  # Сытость героя в [%]
indicator_satiety = Indicator('Сытость', screen, satiety_percent, 0, 0)  # Объект индикатора сытости

while game.status != 'finished':  # Пока игра не завершена
    game.update_logic()
    game.update_graphics()
    forest.hero_x = hero.x  # Координата x героя в [м]
    forest.hero_y = hero.y  # Координата y героя в [м]
    forest.process()
    hero.process()
    satiety_percent: float = 100 * hero.satiety / hero.satiety_max  # Сытость героя в [%]
    indicator_satiety.value = satiety_percent  # Значение индикатора сытости в [%]
    indicator_satiety.process()
