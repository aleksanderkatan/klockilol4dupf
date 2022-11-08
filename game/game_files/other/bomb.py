import game_files.imports.all_sprites as s
import pygame
from game_files.blocks.block_empty import block_empty
import game_files.imports.utils as u
from game_files.imports.log import log
from game_files.imports.view_constants import global_view_constants as v
import game_files.imports.globals as g

font_scale = 1 / 4
FONT = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", int(v.BLOCK_X_SIZE * font_scale))


class bomb:
    def __init__(self, screen, stage, state_index, pos, ticks):
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.ticks = ticks
        self.pos = pos
        self.sprite = s.sprites["bomb"]
        self.finished = False

    def move(self):
        state = self.stage.states[self.state_index]
        player = state.player
        if self.pos == player.pos:
            log.trace("Bomb kicked")
            particle_generator = self.stage.particle_generator
            x, y = u.index_to_position(self.pos[0], self.pos[1], self.pos[2], state.x, state.y, len(state.layers))
            particle_generator.generate_bomb((x, y), player.last_move_direction)
            self.finished = True

        if self.finished:
            return

        self.ticks -= 1
        if self.ticks == 0:
            log.trace("Bomb exploded")
            state.set_block(self.pos, block_empty(self.screen, self.stage, self.state_index, self.pos))
            x, y = u.index_to_position(self.pos[0], self.pos[1], self.pos[2], state.x, state.y, len(state.layers))
            self.stage.particle_generator.generate_dust(g.THUNDER_PARTICLES * 2,
                                                        (x + v.BLOCK_X_SIZE // 2, y + v.BLOCK_Y_SIZE // 2))
            self.finished = True

    def copy(self, new_state_index):
        return bomb(self.screen, self.stage, new_state_index, self.pos, self.ticks)

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)
            txt_surface = FONT.render(str(self.ticks), True, pygame.Color('white'))
            x, y = pos
            off = (1 - font_scale) / 2
            if self.ticks < 10:
                x = x + off * v.BLOCK_X_SIZE
            elif self.ticks < 100:
                x = x + off * v.BLOCK_X_SIZE - font_scale * v.BLOCK_X_SIZE * 0.25
            else:
                x = x + off * v.BLOCK_X_SIZE - font_scale * v.BLOCK_X_SIZE * 0.5
            y = y + off * v.BLOCK_Y_SIZE
            self.screen.blit(txt_surface, (x, y))
