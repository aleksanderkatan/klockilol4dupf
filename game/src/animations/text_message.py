import pygame

from src.imports.view_constants import global_view_constants as v
from src.logic.modes.text_display_utils import create_text_surfaces, horizontal, vertical


class text_message:
    def __init__(self, screen, message, lifetime):
        self.screen = screen
        # self.surfaces_with_poses = create_text_surfaces(message, 0.5, pygame.Color('black'),
        #                                                 (0.5, 0.02), (horizontal.MID, vertical.TOP), horizontal.MID)
        self.surfaces_with_poses = create_text_surfaces(message, 0.5, pygame.Color('black'),
                                                        (0.02, 0.98), (horizontal.LFT, vertical.BOT), horizontal.LFT)
        self.lifetime = lifetime

    def draw(self):
        for surface, pos in self.surfaces_with_poses:
            self.screen.blit(surface, pos)

    def advance(self):
        self.lifetime -= 1

    def has_ended(self):
        return self.lifetime < 0
