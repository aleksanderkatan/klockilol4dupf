import pygame as pg

import src.imports.globals as g
import src.imports.keybindings as k
from src.imports.view_constants import global_view_constants as v
import src.imports.all_sprites as s


COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font("src/fonts/mono/ttf/JetBrainsMono-Regular.ttf", v.WITCH_FONT_SIZE)


class control_display:
    def __init__(self, language):
        pass
        # self.text = text
        # self.txt_surface = FONT.render(text, True, self.color)


    def draw(self, screen):
        screen.blit(s.sprites['background_black'], (0, 0))
