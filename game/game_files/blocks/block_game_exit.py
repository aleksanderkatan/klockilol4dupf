from game_files.blocks.block import block
from game_files.logic.commands import exit_game
import game_files.imports.all_sprites as s


class block_game_exit(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_end"]

    def copy(self, new_state_index):
        return block_game_exit(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        exit_game()
