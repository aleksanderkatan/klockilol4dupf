import abc

import pygame

from src.logic.modes.text_display_utils import create_text_surfaces, horizontal, vertical


class speedrun(metaclass=abc.ABCMeta):
    def __init__(self, settings):
        self.settings = settings
        self.text_sprite_with_pos = None

    def get_starting_stage_and_pos(self):
        pass

    def is_condition_met(self):
        pass

    def get_name(self):
        pass

    def does_death_reset(self):
        pass

    def get_text_sprite_and_pos(self):
        if self.text_sprite_with_pos is None:
            self.text_sprite_with_pos = create_text_surfaces(
                f"Speedrun: {self.get_name()}", 0.5, pygame.Color('black'),
                (0.98, 0.98), (horizontal.RGT, vertical.BOT),
                horizontal.RGT,
            )[0]
        return self.text_sprite_with_pos
