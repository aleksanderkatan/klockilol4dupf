import math

import pygame

import src.imports.all_sprites as s
import src.imports.utils as u
from src.imports.view_constants import global_view_constants as v
from src.blocks.impure.block_perma_unsteppable import block_perma_unsteppable


class block_temmie(block_perma_unsteppable):
    def draw(self, pos, where_is_player):
        super().draw(pos, where_is_player)

        center_pos = pos[0] + v.BLOCK_X_SIZE/2, pos[1] + v.BLOCK_Y_SIZE/2
        state = self.stage.states[self.state_index]
        player_pos_in_state = state.player.pos
        player_pos = u.index_to_position(player_pos_in_state[0], player_pos_in_state[1], player_pos_in_state[2],
                                         state.x, state.y, state.z)
        angle = math.degrees(math.atan2(-(player_pos[1]-pos[1]), (player_pos[0]-pos[0])))
        temmie_sprite = s.sprites["decoration_1x1_temmie"][where_is_player]
        rot_sprite = pygame.transform.rotate(temmie_sprite, angle)
        sprite_pos = center_pos[0]-rot_sprite.get_size()[0]/2, center_pos[1]-rot_sprite.get_size()[1]/2
        self.screen.blit(rot_sprite, sprite_pos)

    def copy(self, new_state_index):
        return block_temmie(self.screen, self.stage, new_state_index, self.pos)
