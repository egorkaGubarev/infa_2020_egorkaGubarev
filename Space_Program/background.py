class Background:

    def __init__(self):

        self.color: tuple = (0, 128, 0)

    def draw(self, screen):

        color: tuple = self.color

        screen.fill(color)
