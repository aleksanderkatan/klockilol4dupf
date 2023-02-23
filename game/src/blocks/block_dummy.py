import src.imports.all_sprites as s
from src.blocks.block import block
from src.blocks.block_empty import block_empty


class block_dummy(block):
    def __init__(self, screen, stage, state_index, pos, ):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites['block_dummy']

    def copy(self, new_state_index):
        return block_dummy(self.screen, self.stage, new_state_index, self.pos)

    def replaced_with(self):
        return block_empty(self.screen, self.stage, self.state_index, self.pos)

    def on_step_out(self):
        x, y, z = self.pos
        self.stage.states[self.state_index].layers[z].grid[x][y] = self.replaced_with()
