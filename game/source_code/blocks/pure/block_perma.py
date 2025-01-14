import source_code.imports.all_sprites as s
from source_code.blocks.block import block


class block_perma(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]

    def copy(self, new_state_index):
        return block_perma(self.screen, self.stage, new_state_index, self.pos)
