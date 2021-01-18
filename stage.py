import pygame
from state import state
import utils as u
import levels as l

FONT = pygame.font.Font("fonts/mono/ttf/JetBrainsMono-Regular.ttf", 64)

class stage:
    def __init__(self, screen, level_index, last_level_index):
        self.screen = screen
        self.states = []
        first_state = state(screen, self, 0)
        self.level_index = level_index
        first_state.fill(l.levels(self.level_index), last_level_index)
        self.states.append(first_state)
        self.change_to = None

    def draw(self, single_layer=None):
        if single_layer is None:
            self.latest_state().draw()
        else:
            self.latest_state().draw_one_layer(single_layer)
        txt_surface = FONT.render(l.level_name(self.level_index), True, pygame.Color('black'))
        self.screen.blit(txt_surface, (16, 16))

    def latest_state(self):
        return self.states[len(self.states) - 1]

    def move(self, direction=None):
        if direction is None and not self.latest_state().player.has_something_enqueued():
            return

        if self.latest_state().player.dead:
            return
        new_state = self.latest_state().copy(len(self.states))
        self.states.append(new_state)
        new_state.move(direction)

    def reverse(self):
        if len(self.states) > 1:
            del self.states[-1]
            while self.states[-1].is_next_move_forced():
                del self.states[-1]

    def reset(self):
        self.states = self.states[0:1]

    def needs_input(self):
        return not self.latest_state().is_next_move_forced()

    def get_player_index(self):
        return self.latest_state().player.pos
