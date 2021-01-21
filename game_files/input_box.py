import pygame as pg
import game_files.config as c

COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
FONT = pg.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", c.WITCH_FONT_SIZE)

class input_box:
    def __init__(self, x, y, w, h, stage, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.stage = stage
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.key == pg.K_RSHIFT:
            self.active = False
            self.text = ''

        if event.key == pg.K_RETURN:
            self.active = not self.active
            if not self.active:
                self.stage.execute_command(self.text)
            self.text = ''

        if not self.active:
            return
        elif event.key == pg.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            if len(self.text) < c.MAX_COMMAND_LENGTH and event.key != pg.K_RETURN:
                self.text += event.unicode
        self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+c.WITCH_FONT_OFFSET, self.rect.y+c.WITCH_FONT_OFFSET*0.5)) # !! another constant
        pg.draw.rect(screen, self.color, self.rect, 2)
