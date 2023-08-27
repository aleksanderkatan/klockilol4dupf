import src.imports.all_sprites as s
from src.blocks.block import block
from src.blocks.semi_pure.block_swapping import block_swapping


class block_swapping_trigger(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_swapping_trigger"]

    def copy(self, new_state_index):
        return block_swapping_trigger(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        for blo in state.block_iterator():
            if issubclass(type(blo), block_swapping):
                blo.change_state()
