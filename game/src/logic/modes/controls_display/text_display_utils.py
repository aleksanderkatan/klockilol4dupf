from enum import Enum
import pygame as pg

from src.imports.view_constants import global_view_constants as v


class horizontal(Enum):
    LFT = -1
    MID = 0
    RGT = 1


class vertical(Enum):
    TOP = -1
    MID = 0
    BOT = 1



def create_text_surfaces(multiline_text, font_multiplier, color, pos, rel=(horizontal.LFT, vertical.TOP), align=horizontal.LFT):
    font = pg.font.Font(v.FONT_PATH, v.WITCH_FONT_SIZE * font_multiplier)
    surfaces_with_sizes = []
    anchor_x, anchor_y = pos[0] * v.WINDOW_X, pos[1] * v.WINDOW_Y
    rel_x, rel_y = rel
    total_width = 0
    total_height = 0
    for i, line in enumerate(multiline_text.split("\n")):
        surface = font.render(line, True, color)
        sur_x, sur_y = font.size(line)
        if sur_x > total_width:
            total_width = sur_x
        total_height += sur_y
        surfaces_with_sizes.append((surface, (sur_x, sur_y)))

    first_x = anchor_x + (-rel_x.value - 1) * total_width // 2
    first_y = anchor_y + (-rel_y.value - 1) * total_height // 2

    surfaces_with_positions = []
    for i, (surface, size) in enumerate(surfaces_with_sizes):
        pos_x = first_x + (total_width - size[0]) // 2 * (align.value+1)
        pos_y = first_y + i * size[1]
        surfaces_with_positions.append((surface, (pos_x, pos_y)))


    return surfaces_with_positions






