import pygame

from src.utils.config import Config
_C = Config.conf


class DebugLines:
    def __init__(self, surface):
        self.x = 20
        self.y = 20
        self.surface = surface

        # Lines
        self.hline_start = (0, self.y)
        self.hline_stop = (_C("WIDTH"), self.y)
        self.vline_start = (self.x, 0)
        self.vline_stop = (self.x, _C("HEIGHT"))
        self.color = _C("colors", "WHITE")
        self.color_h = _C("colors", "BLUE")
        self.color_v = _C("colors", "BLUE")
        self.snap = False

        # Text
        self.f16 = pygame.font.Font(None, 16)

        # Rect
        self.draw_rect = False
        self.oldx = 0
        self.oldy = 0
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.text_x = 0
        self.text_y = 0
        self.text_surface_select = None

    def update(self, x, y):
        if _C("DEBUG"):
            # Lines
            if self.snap:
                if (_C("WIDTH") // 2 - 10) <= x <= (_C("WIDTH") // 2 + 10):
                    self.x = _C("WIDTH") // 2
                    self.color_v = _C("colors", "GREEN")
                else:
                    self.x = x
                    self.color_v = _C("colors", "BLUE")
                if (_C("HEIGHT") // 2 - 10) <= y <= (_C("HEIGHT") // 2 + 10):
                    self.y = _C("HEIGHT") // 2
                    self.color_h = _C("colors", "GREEN")
                else:
                    self.y = y
                    self.color_h = _C("colors", "BLUE")
            else:                    
                self.x = x
                self.color_v = _C("colors", "BLUE")
                self.y = y
                self.color_h = _C("colors", "BLUE")

            self.hline_start = (0, self.y)
            self.hline_stop = (_C("WIDTH"), self.y)

            self.vline_start = (self.x, 0)
            self.vline_stop = (self.x, _C("HEIGHT"))

            # Rect
            if not self.draw_rect:
                self.oldx, self.oldy = pygame.mouse.get_pos()
                self.rect.x = 0
                self.rect.y = 0
                self.rect.width = 0
                self.rect.height = 0

            if self.draw_rect:
                self.draw_rect_text()
                if self.x >= self.oldx:
                    self.rect.x = self.oldx
                    self.rect.width = self.x - self.oldx
                    self.text_x = self.x - self.rect.width // 2 - self.text_surface_select.get_width() // 2
                    if self.y >= self.oldy:
                        self.rect.y = self.oldy
                        self.rect.height =  self.y - self.oldy
                        self.text_y = self.y - self.rect.height // 2 - self.text_surface_select.get_height() // 2
                    else:
                        self.rect.y = self.y
                        self.rect.height = self.oldy - self.y
                        self.text_y = self.y + self.rect.height // 2 - self.text_surface_select.get_height() // 2
                elif self.x <= self.oldx:
                    self.rect.x = self.x
                    self.rect.width = self.oldx - self.x
                    self.text_x = self.x + self.rect.width // 2  - self.text_surface_select.get_width() // 2
                    if self.y <= self.oldy:
                        self.rect.y = self.y
                        self.rect.height =  self.oldy - self.y
                        self.text_y = self.oldy - self.rect.height // 2 - self.text_surface_select.get_height() // 2
                    else:
                        self.rect.y = self.oldy
                        self.rect.height =  self.y - self.oldy
                        self.text_y = self.oldy + self.rect.height // 2 - self.text_surface_select.get_height() // 2

    def draw_text(self):
        # Coords
        text_surface_coord = self.f16.render(f"{self.x}, {self.y}", True, _C("colors", "WHITE"))
        self.surface.blit(text_surface_coord, (self.x + 10, self.y - 15))
        
        # Width
        text_surface_width = self.f16.render(f'{_C("WIDTH")}', True, _C("colors", "WHITE"))
        self.surface.blit(text_surface_width, (_C("WIDTH") - text_surface_width.get_width() - 5, self.y - 15))
        
        # Height
        text_surface_height = self.f16.render(f'{_C("HEIGHT")}', True, _C("colors", "WHITE"))
        self.surface.blit(text_surface_height, (self.x + 10, 5))

    def draw_rect_text(self):
        self.text_surface_select = self.f16.render(f'{self.rect.width}x{self.rect.height}', True, _C("colors", "CYAN"))
        self.surface.blit(self.text_surface_select, (self.text_x, self.text_y))


    def draw(self):
        if _C("DEBUG"):
            pygame.draw.line(self.surface, self.color_h, self.hline_start, self.hline_stop)
            pygame.draw.line(self.surface, self.color_v, self.vline_start, self.vline_stop)
            self.draw_text()

            pygame.draw.rect(self.surface, self.color, self.rect, 1)
            if self.draw_rect:
                self.draw_rect_text()