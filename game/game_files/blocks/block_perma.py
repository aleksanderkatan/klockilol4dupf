from game_files.blocks.block import block
import game_files.imports.all_sprites as s


class block_perma(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]

    def copy(self, new_state_index):
        return block_perma(self.screen, self.stage, new_state_index, self.pos)
