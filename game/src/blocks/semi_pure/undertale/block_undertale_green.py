import src.imports.all_sprites as s
from src.blocks.pure.block_perma import block_perma


class block_undertale_green(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_jump_2"]

    def copy(self, new_state_index):
        return block_undertale_green(self.screen, self.stage, new_state_index, self.pos)
