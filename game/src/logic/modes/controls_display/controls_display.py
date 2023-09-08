import pygame as pg

import src.imports.all_sprites as s
from src.logic.modes.text_display_utils import create_text_surfaces, horizontal, vertical
from src.strings.translation_getters import get_control_display_strings

COLOR = pg.Color('lightskyblue3')


def _draw_surfaces(screen, surfaces):
    for surface, pos in surfaces:
        screen.blit(surface, pos)


class controls_display:
    def __init__(self, language):
        st = get_control_display_strings(language)
        self.surfaces = []
        self.surfaces += create_text_surfaces(
            st.title_left,
            2,
            COLOR,
            (0.25, 0.1),
            (horizontal.MID, vertical.MID)
        )
        self.surfaces += create_text_surfaces(
            st.title_right,
            2,
            COLOR,
            (0.75, 0.1),
            (horizontal.MID, vertical.MID)
        )
        self.surfaces += create_text_surfaces(
            st.left,
            1,
            COLOR,
            (0.25, 0.2),
            (horizontal.MID, vertical.TOP)
        )
        self.surfaces += create_text_surfaces(
            st.right,
            0.75,
            COLOR,
            (0.73, 0.2),
            (horizontal.MID, vertical.TOP)
        )
        self.surfaces += create_text_surfaces(
            st.bottom,
            1,
            COLOR,
            (0.5, 0.82),
            (horizontal.MID, vertical.TOP)
        )

    def draw(self, screen):
        screen.blit(s.sprites['background_blacker'], (0, 0))
        _draw_surfaces(screen, self.surfaces)
