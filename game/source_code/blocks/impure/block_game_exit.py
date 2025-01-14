import source_code.imports.all_sprites as s
import source_code.imports.globals as g
from source_code.blocks.block import block
from source_code.imports.log import log
from source_code.logic.commands import exit_game


class block_game_exit(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_end"]

    def copy(self, new_state_index):
        return block_game_exit(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        log.write(g.save_state.get_all_stats())
        exit_game()
