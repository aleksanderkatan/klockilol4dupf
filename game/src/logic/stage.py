import pygame
from src.logic.state import state
import src.imports.globals as g
import src.imports.levels as l
from src.imports.view_constants import global_view_constants as v
from src.other.particle_generator import particle_generator
from src.imports.log import log
from src.logic.state_filler.state_filler_uno_duo import fill
from src.animations.animation_manager import animation_manager
from src.logic.direction import direction as d

FONT = pygame.font.Font("src/fonts/mono/ttf/JetBrainsMono-Regular.ttf", v.LEVEL_FONT_SIZE)


class stage:
    def __init__(self, screen, level_index, last_level_index):
        self.screen = screen
        self.states = []
        first_state = state(screen, self, 0)
        self.level_index = level_index
        self.successful = fill(first_state, level_index, last_level_index)
        self.speedrun_check_needed = False
        if self.successful:
            self.states.append(first_state)
            first_state.update_dark_visibility()
        self.change_to = None
        self.particle_generator = particle_generator(self.screen)
        self.animation_manager = animation_manager()
        self.name_surface = FONT.render(l.level_name(self.level_index), True, pygame.Color('black'))


    def draw(self, single_layer=None):
        if single_layer is None:
            self.latest_state().draw()
        else:
            self.latest_state().draw_one_layer(len(self.latest_state().layers) - single_layer - 1)
        self.particle_generator.step()
        self.particle_generator.draw()
        self.animation_manager.draw_and_advance()
        if not self.latest_state().player.dead:
            self.screen.blit(self.name_surface, (v.LEVEL_FONT_OFFSET, v.LEVEL_FONT_OFFSET))

    def latest_state(self):
        return self.states[-1]

    def move(self, direction=d.NONE):
        if len(self.states) > g.MOVE_LIMIT:
            log.info('Move limit exceeded, resetting...')
            self.reset()
            return

        if direction == d.NONE and not self.latest_state().player.has_something_enqueued():
            return

        if self.latest_state().player.dead:
            return

        if self.animation_manager.is_logic_prevented():
            return

        old_state = self.latest_state()
        new_state = old_state.copy(len(self.states))
        self.states.append(new_state)
        new_state.move(direction)
        if new_state.invalid:
            log.trace("Invalid move performed")
            self.soft_reverse()
            return

    def soft_reverse(self):
        if len(self.states) > 1:
            del self.states[-1]
            self.latest_state().player.set_next_move_direction(d.NONE)

    def reverse(self):
        if len(self.states) > 1:
            del self.states[-1]
            while self.states[-1].is_next_move_forced():
                del self.states[-1]
        self.particle_generator.reset()
        self.animation_manager.reset()

    def reset(self):
        self.states = self.states[0:1]
        self.particle_generator.reset()

    def needs_input(self):
        return not self.latest_state().is_next_move_forced()

    def get_player_index(self):
        return self.latest_state().player.pos
