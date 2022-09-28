from game_files.animations.animation import animation
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v
import game_files.imports.utils as u
import pygame

class animation_disappearing_block(animation):
    def __init__(self, screen, stage, state_index, sprite, pos=None, screen_pos=None):
        self.screen = screen
        self.stage = stage
        self.state = stage.states[state_index]
        self.sprite = sprite
        self.positions = []
        self.sizes = []
        state = stage.states[state_index]
        if screen_pos is not None:
            x, y = screen_pos
        else:
            x, y = u.index_to_position(pos[0], pos[1], pos[2], state.x, state.y, state.z)

        L = g.DISAPPEAR_ANIMATION_LENGTH
        unit_x = v.BLOCK_X_SIZE/(2*L)
        unit_y = v.BLOCK_Y_SIZE/(2*L)
        for i in range(L):
            self.positions.append((x + i*unit_x, y + i*unit_y))
            scale = (L-i)/L
            self.sizes.append((int(v.BLOCK_X_SIZE * scale), int(v.BLOCK_Y_SIZE * scale)))
        self.frame = 0

    def draw(self):
        i = min(self.frame, len(self.positions))
        im = pygame.transform.scale(self.sprite, self.sizes[i])
        self.screen.blit(im, self.positions[i])

    def advance(self):
        self.frame += 1

    def prevents_logic(self):
        return False

    def has_ended(self):
        return self.frame >= len(self.positions)

    def is_persistent(self):
        return False
