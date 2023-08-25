import pygame as pg

import src.imports.globals as g
import src.imports.keybindings as k
from src.imports.view_constants import global_view_constants as v
import src.imports.all_sprites as s
from src.logic.modes.controls_display.text_display_utils import create_text_surfaces, horizontal, vertical

COLOR = pg.Color('lightskyblue3')


def _draw_surfaces(screen, surfaces):
    for surface, pos in surfaces:
        screen.blit(surface, pos)


class control_display:
    def __init__(self, language):
        self.title_surfaces = create_text_surfaces(
            "kontrolki",
            2,
            COLOR,
            (0.5, 0.1),
            (horizontal.MID, vertical.MID)
        )
        self.left_surfaces = create_text_surfaces(
            "WSAD - chodzenie\n" +
            "Q - undo\n" +
            "R - reset\n" +
            "bbbbb",
            1,
            COLOR,
            (0.25, 0.2),
            (horizontal.MID, vertical.TOP)
        )
        self.right_surfaces = create_text_surfaces(
            "Enter - konsola\n" +
            "W konsoli możesz wpisywać\nróżne komendy.\n" +
            "R - reset\n" +
            "AAAAAAAAAAAAAAA\n" +
            "bbbbb",
            1,
            COLOR,
            (0.75, 0.2),
            (horizontal.MID, vertical.TOP)
        )

    def draw(self, screen):
        screen.blit(s.sprites['background_black'], (0, 0))
        _draw_surfaces(screen, self.title_surfaces)
        _draw_surfaces(screen, self.left_surfaces)
        _draw_surfaces(screen, self.right_surfaces)
