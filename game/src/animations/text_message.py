import pygame

from src.imports.view_constants import global_view_constants as v

FONT = pygame.font.Font("src/fonts/mono/ttf/JetBrainsMono-Regular.ttf", v.MESSAGE_FONT_SIZE)


class text_message:
    def __init__(self, screen, message, lifetime):
        self.screen = screen

        self.surface = FONT.render(message, True, pygame.Color('black'))
        self.pos = (v.WINDOW_X // 2 - self.surface.get_rect().width // 2, v.MESSAGE_FONT_SIZE)
        self.lifetime = lifetime

    def draw(self):
        self.screen.blit(self.surface, self.pos)

    def advance(self):
        self.lifetime -= 1

    def has_ended(self):
        return self.lifetime < 0
