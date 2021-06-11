import pygame
from game_files.logic.state import state
import game_files.imports.globals as g
import game_files.imports.levels as l
from game_files.imports.view_constants import global_view_constants as v
from game_files.other.particle_generator import particle_generator
from game_files.imports.log import log


FONT = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", v.LEVEL_FONT_SIZE)

class stage:
    def __init__(self, screen, level_index, last_level_index):
        self.screen = screen
        self.states = []
        first_state = state(screen, self, 0)
        self.level_index = level_index
        self.successful = first_state.fill(l.levels(self.level_index), last_level_index)
        if self.successful is False:
            log.error("Stage " + str(level_index) + " failed to load")
        else:
            self.states.append(first_state)
            first_state.update_dark_visibility()
        self.change_to = None
        self.particle_generator = particle_generator(self.screen)

    def draw(self, single_layer=None):
        if single_layer is None:
            self.latest_state().draw()
        else:
            self.latest_state().draw_one_layer(len(self.latest_state().layers)-single_layer-1)
        self.particle_generator.step()
        self.particle_generator.draw()
        txt_surface = FONT.render(l.level_name(self.level_index), True, pygame.Color('black'))
        if not self.latest_state().player.dead:
            self.screen.blit(txt_surface, (v.LEVEL_FONT_OFFSET, v.LEVEL_FONT_OFFSET))

    def latest_state(self):
        return self.states[len(self.states) - 1]

    def move(self, direction=None):
        if len(self.states) > g.MOVE_LIMIT:
            log.warning('Move limit exceeded, resetting...')
            self.reset()
            return

        if direction is None and not self.latest_state().player.has_something_enqueued():
            return

        if self.latest_state().player.dead:
            return
        new_state = self.latest_state().copy(len(self.states))
        self.states.append(new_state)
        new_state.move(direction)
        if new_state.invalid:
            log.info("Invalid move performed")
            self.soft_reverse()

    def soft_reverse(self):
        if len(self.states) > 1:
            del self.states[-1]
            self.latest_state().player.set_next_move_direction(None)

    def reverse(self):
        if len(self.states) > 1:
            del self.states[-1]
            while self.states[-1].is_next_move_forced():
                del self.states[-1]
        self.particle_generator.reset()

    def reset(self):
        self.states = self.states[0:1]
        self.particle_generator.reset()

    def needs_input(self):
        return not self.latest_state().is_next_move_forced()

    def get_player_index(self):
        return self.latest_state().player.pos
