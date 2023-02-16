from src.blocks.block import block
from src.logic.commands import exit_game
import src.imports.all_sprites as s
from src.imports.log import log
from src.imports.save_state import global_save_state


class block_game_exit(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_end"]

    def copy(self, new_state_index):
        return block_game_exit(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        log.write(global_save_state.get_all_stats())
        exit_game()
