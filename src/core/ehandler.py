import pygame

from src.utils.config import Config
_C = Config.conf

class EHandler:
    def __init__(self) -> None:
        pass

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # Mouse Events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mouse.set_visible(False)
                    self.dlines.draw_rect = True
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pygame.mouse.set_visible(True)
                    self.dlines.draw_rect = False
            # Key Events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    self.dlines.snap = True
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    self.dlines.snap = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.update("left", self.speed)
        if keys[pygame.K_d]:
            self.player.update("right", self.speed)