from src.blocks.block import block
from src.blocks.block_swapping import block_swapping
import src.imports.all_sprites as s
import random


# maybe should be a variant of block_swapping_trigger?
class block_swapping_trigger_random(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_swapping_trigger"]

    def copy(self, new_state_index):
        return block_swapping_trigger_random(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        for blo in state.block_iterator():
            if issubclass(type(blo), block_swapping):
                blo.set_state(True if random.randint(0, 1) == 0 else False)
