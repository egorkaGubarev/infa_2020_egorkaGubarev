"""
Модуль игры
"""

import pygame


class Game(object):
    """
    Описывает игру
    """

    def __init__(self, screen):
        """
        Параметры

        Графика
        screen - экран pygame
        """

        # Логика
        self.clock = pygame.time.Clock()  # Часы pygame
        self.status: str = 'created'  # Игра созднана

        # Графика
        self.black: tuple = (0, 0, 0)  # Чёрный цвет
        self.fps: int = 24  # Частота обновления экарана в [Гц]
        self.screen = screen

        # Физика
        self.day_length: int = 600  # Длинна дня в [с]
        self.time_step: float = 1 / self.fps  # Квант времени в [с]

    # --- Логика ---
    def update_logic(self):
        """
        Обрабатывает логические события
        """

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Если нажата клавиша
                if event.key == pygame.K_ESCAPE:  # Если нажат Esc
                    self.status: str = 'finished'  # Игра завершена

    # --- Графика ---
    def update_graphics(self):

        # Логика
        clock = self.clock  # Часы pygame

        # Графика
        black: tuple = self.black  # Чёрный чвет
        fps: int = self.fps  # Частота обновления экрана в [Гц]
        screen = self.screen  # Экран pygame

        pygame.display.update()
        clock.tick(fps)
        screen.fill(black)
