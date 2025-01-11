import math

import pygame

import src.imports.all_sprites as s
import src.imports.utils as u
from src.imports.view_constants import global_view_constants as v
from src.blocks.impure.block_perma_unsteppable import block_perma_unsteppable


def _find_angle(state, pos):
    player_pos_in_state = state.player.pos
    player_pos = u.index_to_position(player_pos_in_state[0], player_pos_in_state[1], player_pos_in_state[2],
                                     state.x, state.y, state.z)
    return math.degrees(math.atan2(-(player_pos[1] - pos[1]), (player_pos[0] - pos[0])))


def _rotate(pos, where_is_player, state):
    if where_is_player is None:
        return
    angle = _find_angle(state, pos)
    temmie_sprite = s.sprites["decoration_1x1_temmie"][where_is_player].copy()
    rot_sprite = pygame.transform.rotate(temmie_sprite, angle)
    center_pos = pos[0] + v.BLOCK_X_SIZE / 2, pos[1] + v.BLOCK_Y_SIZE / 2
    sprite_pos = center_pos[0] - rot_sprite.get_size()[0] / 2, center_pos[1] - rot_sprite.get_size()[1] / 2
    return sprite_pos, rot_sprite


class block_temmie(block_perma_unsteppable):
    def __init__(self, screen, stage, state_index, pos, sprite_cache=None):
        super().__init__(screen, stage, state_index, pos)
        if sprite_cache is None:
            sprite_cache = {}
        self.sprite_cache = sprite_cache

    def draw(self, pos, where_is_player):
        super().draw(pos, where_is_player)
        if where_is_player is None:
            return

        state = self.stage.states[self.state_index]
        player_pos = state.player.pos
        if player_pos not in self.sprite_cache:
            self.sprite_cache[player_pos] = _rotate(pos, where_is_player, state)

        sprite_pos, rot_sprite = self.sprite_cache[player_pos]
        self.screen.blit(rot_sprite, sprite_pos)

    def copy(self, new_state_index):
        return block_temmie(self.screen, self.stage, new_state_index, self.pos, self.sprite_cache)
