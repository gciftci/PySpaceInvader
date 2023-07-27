import pygame

from src.utils.config import Config
_C = Config.conf

class UpdateHandler:
    def __init__(self) -> None:
        pass

    def update(self):
        x,y = pygame.mouse.get_pos()
        self.dlines.update(x,y)
        