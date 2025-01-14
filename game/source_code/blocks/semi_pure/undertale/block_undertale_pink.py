import source_code.imports.all_sprites as s
from source_code.blocks.pure.block_perma import block_perma


class block_undertale_pink(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pink"]

    def copy(self, new_state_index):
        return block_undertale_pink(self.screen, self.stage, new_state_index, self.pos)
