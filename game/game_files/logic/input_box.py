import pygame as pg
import game_files.imports.globals as g
import game_files.imports.keybindings as k
from game_files.imports.view_constants import global_view_constants as v

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", v.WITCH_FONT_SIZE)

class input_box:
    def __init__(self, x, y, w, h, stage, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.stage = stage
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_key_pressed(self, key, unicode):
        if k.is_input_box_disable(key):
            self.active = False
            self.text = ''
        elif k.is_input_box_enable(key):
            self.active = not self.active
            if not self.active:
                self.stage.execute_command(self.text)
            self.text = ''
        elif not self.active:
            return
        elif k.is_input_box_delete(key):
            self.text = self.text[:-1]
        elif len(self.text) < g.MAX_COMMAND_LENGTH and not k.is_input_box_enable(key):
            self.text += unicode

        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+v.WITCH_FONT_OFFSET, self.rect.y+v.WITCH_FONT_OFFSET*0.5))   # !! another constant
        pg.draw.rect(screen, self.color, self.rect, 2)
