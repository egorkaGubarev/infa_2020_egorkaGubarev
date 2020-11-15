"""
Главный модуль
"""

import pygame

from game import Game
from hero import Hero

# Графика
screen_height: int = 700  # Высота экрана в пикселях
screen_width: int = 1200  # Ширина экрана в пикселях

# Объекты
game = Game()  # Объект игры
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)  # Объект экрана pygame
hero = Hero(screen)  # Объект героя

while game.status != 'finished':  # Пока игра не завершена
    game.update_logic()
