from game_files.blocks.block import block
import game_files.all_sprites as s
from game_files.save_state import global_save_state

class block_shrek(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]
        self.player_sprite = {}
        self.player_sprite[True] = s.sprites["player"][0]
        self.player_sprite[False] = s.sprites["player_shrek"][0]

    def copy(self, new_state_index):
        return block_shrek(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        global_save_state.change_shrek()

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)
            self.screen.blit(self.player_sprite[global_save_state.is_shrek()], pos)


