import pygame


class Game:

    def __init__(self):

        self.clock = pygame.time.Clock()
        self.fps: int = 24  # in [Hz]
        self.screen_height: int = 700  # in [px]
        self.screen_width: int = 1200  # in [px]
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        self.status: str = 'create'

    def setup(self):

        self.status = 'run'

    def update_logic(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.status: str = 'exit'
