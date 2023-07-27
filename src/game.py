import pygame

# Utilities
from src.utils.config import Config
from src.utils.tools import DebugLines

# Logic-Handler
from src.core.ehandler import EHandler
from src.core.drawhandler import DrawHandler
from src.core.updatehandler import UpdateHandler

# Objects
from src.objects.player import Player
from src.utils.ui import Text

_C = Config.conf

class Game:
    def __init__(self):
        # General
        pygame.init()
        self.main_surface = pygame.display.set_mode((_C("WIDTH"), _C("HEIGHT")), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        self.running = True
        self.speed = 0
        # Debug
        self.dlines = DebugLines(self.main_surface)

        # Init Objects
        self.player = Player(_C("WIDTH") // 2, _C("HEIGHT") - 100)
        self.text = Text()

    def run(self):
        while self.running:
            EHandler.event_handler(self)
            UpdateHandler.update(self)
            DrawHandler.draw(self)

            dt = self.clock.tick(_C("FPS"))
            self.speed = 1 / float(dt)
            
        pygame.quit()
