import pygame
import math
import random

from src.utils.config import Config
_C = Config.conf


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x -10, y, 20, 20)
        self.speed = 200

        # Weapon
        # TODO: Implement Weapons
        self.weapon_type = 1
        self.fire_rate = 1

    def update(self, pos, dt):
        # TODO: Proper dt-Movement (Framerate indepent)
        mx = (self.speed * dt)
        if pos == "left":
            if self.rect.x - mx > 0:
                self.rect.x -= mx
            else:
                self.rect.x = 0
        else:
            if (self.rect.x + 20 + mx) < _C("WIDTH"):
                self.rect.x += mx
            else:
                self.rect.x = _C("WIDTH") - 20

    def draw(self, window):
        pygame.draw.rect(window, _C("colors", "BLUE"), self.rect)
