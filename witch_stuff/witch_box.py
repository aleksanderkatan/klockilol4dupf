import pygame as pg
import config as c

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(None, 100)

class witch_box:
    def __init__(self, x, y, w, h, screen, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.screen = screen
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def set_text(self, text):
        self.text = text
        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self):
        self.screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(self.screen, self.color, self.rect, 2)
