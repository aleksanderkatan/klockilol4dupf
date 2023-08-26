import pygame as pg

import src.imports.globals as g
import src.imports.keybindings as k
from src.imports.view_constants import global_view_constants as v
import src.imports.all_sprites as s


COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font(v.FONT_PATH, v.WITCH_FONT_SIZE)


def censor_text(text):
    for command_name in g.ENABLE_CHEATS_COMMANDS:
        if text[:len(command_name)] == command_name:
            return command_name + " " + "*" * (len(text) - len(command_name) - 1)
    return text


class input_box:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)

    def handle_key_pressed(self, key, unicode):
        if k.is_input_box_delete(key):
            self.text = self.text[:-1]
        elif len(self.text) < g.MAX_COMMAND_LENGTH:
            self.text += unicode
        self.txt_surface = FONT.render(censor_text(self.text), True, self.color)

    def clear(self):
        self.text = ""
        self.txt_surface = FONT.render(self.text, True, self.color)


    def draw(self, screen):
        screen.blit(s.sprites['background_black'], (0, 0))
        screen.blit(self.txt_surface,
                    (self.rect.x + v.WITCH_FONT_OFFSET, self.rect.y + v.WITCH_FONT_OFFSET * 0.5))  # !! another constant
        pg.draw.rect(screen, self.color, self.rect, 2)
