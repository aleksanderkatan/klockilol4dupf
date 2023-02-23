import src.imports.all_sprites as s
from src.blocks.block import block


class block_minus(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_minus"]

    def copy(self, new_state_index):
        return block_minus(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.dark_visibility = max(state.dark_visibility - 1, 0)
