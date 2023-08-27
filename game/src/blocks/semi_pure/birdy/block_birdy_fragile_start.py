import src.imports.all_sprites as s
from src.blocks.block_empty import block_empty
from src.blocks.pure.block_start import block_start


class block_birdy_fragile_start(block_start):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_fragile_start"]

    def on_step_out(self):
        super().on_step_out()
        empty = block_empty(self.screen, self.stage, self.state_index, self.pos)
        self.stage.states[self.state_index].set_block(self.pos, empty)

    def copy(self, new_state_index):
        return block_birdy_fragile_start(self.screen, self.stage, new_state_index, self.pos)
