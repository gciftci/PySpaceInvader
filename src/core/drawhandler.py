import pygame

from src.utils.config import Config
_C = Config.conf

class DrawHandler:
    def __init__(self):
        pass

    def draw(self):
        # Clear Surface
        self.main_surface.fill(_C("BACKGROUND"))

        # Objects
        self.player.draw(self.main_surface)
        self.text.draw(self.main_surface, self.clock)

        # Utilities
        self.dlines.draw()

        # Update
        pygame.display.update()