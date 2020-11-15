"""
Модуль игры
"""

import pygame


class Game(object):
    """
    Описывает игру
    """

    def __init__(self):
        """
        Параметры
        """

        # Логика
        self.status: str = 'created'  # Игра созднана

    # --- Логика ---

    def update_logic(self):
        """
        Обрабатывает логические события
        """

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_ESCAPE:  # Если нажат Esc
                    self.status: str = 'finished'  # Игра завершена
