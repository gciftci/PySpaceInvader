import pygame

from src.utils.config import Config
_C = Config.conf

class Text:
    def __init__(self):
        self.f16 = pygame.font.Font(None, 16)
        self.f20 = pygame.font.Font(None, 20)
        self.f32 = pygame.font.Font(None, 32)

    def get_text_width(self, text, font):
        text_surface = font.render(text, True, _C("colors", "WHITE"))
        return text_surface.get_width()

    def draw_text(self, surface, text, pos, font):
        text_surface = font.render(text, True, _C("colors", "WHITE"))
        surface.blit(text_surface, pos)

    def draw_fps(self, surface, clock):
        self.draw_text(surface, f"FPS: {int(clock.get_fps())}", (10, 10), self.f32)

    def draw(self, surface, clock):
        self.draw_fps(surface, clock)