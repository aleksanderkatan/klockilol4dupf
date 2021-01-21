from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.all_sprites as s

class block_numeric(block):
    def __init__(self, screen, stage, state_index, pos, number=-1):
        super().__init__(screen, stage, state_index, pos)
        self.set_number(number)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_numeric(self.screen, self.stage, new_state_index, self.pos, self.number)

    def replaced_with(self):
        print(self.number)
        if self.number > 1:
            return block_numeric(self.screen, self.stage, self.state_index, self.pos, self.number-1)
        else:
            return block_empty(self.screen, self.stage, self.state_index, self.pos)

    def on_step_out(self):
        x, y, z = self.pos
        self.stage.states[self.state_index].layers[z].grid[x][y] = self.replaced_with()

    def set_number(self, number):
        self.number = number
        if 1 <= number <= 8:
            self.sprite = s.sprites["block_numeric_" + str(number)]
        else:
            self.sprite = s.sprites["error"]
