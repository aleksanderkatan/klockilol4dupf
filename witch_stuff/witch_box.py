import pygame as pg
import config as c

COLOR = pg.Color('lightskyblue3')
COLOR_BACK = pg.Color('black')
FONT_SIZE = c.WITCH_FONT_SIZE
FONT_OFFSET = c.WITCH_FONT_OFFSET
FONT = pg.font.Font("fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE)


class witch_box:
    def __init__(self, screen):
        self.screen = screen
        self.txt_surfaces = []
        self.text = ''
        self.rect = None
        self.active = False

    def set_text(self, text):
        self.text = self.wrap(text)

        self.rect = pg.Rect(
            0, c.WINDOW_Y-FONT_SIZE*len(self.text)-2*FONT_OFFSET, c.WINDOW_X, FONT_SIZE*len(self.text)+2*FONT_OFFSET
        )
        self.txt_surfaces = []
        for string in self.text:
            self.txt_surfaces.append(FONT.render(string, True, COLOR))

    def draw(self):
        pg.draw.rect(self.screen, COLOR_BACK, self.rect)
        pg.draw.rect(self.screen, COLOR, self.rect, 2)
        for i in range(len(self.txt_surfaces)):
            self.screen.blit(
                self.txt_surfaces[i], (self.rect.x + FONT_OFFSET, self.rect.y + i*FONT_SIZE + 0.5*FONT_OFFSET)
            ) # !!wtf this shouldn't work

    def wrap(self, string):
        if string is None:
            return None
        words = string.split(' ')
        result = []
        current = ''
        limit = int((c.WINDOW_X-FONT_OFFSET*2)/(FONT_SIZE*0.59)) # !!stupid constant in code

        for word in words:
            if len(current) + 1 + len(word) <= limit:
                current = current + word + " "
            else:
                result.append(current)
                current = word + " "
        result.append(current)

        return result
