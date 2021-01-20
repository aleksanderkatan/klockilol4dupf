from objects.block import block
import import_sprites as s
from import_objects import block_numeric

class block_ones(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_ones"]

    def copy(self, new_state_index):
        return block_ones(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        x, y, z = self.pos
        poses = [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z)]
        for pos in poses:
            self.stage.states[self.state_index].set_block(pos, block_numeric(self.screen, self.stage, self.state_index, pos, 1))
