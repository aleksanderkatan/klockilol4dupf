from game.game_files.blocks.block import block
from game.game_files.blocks.block_empty import block_empty
import game.game_files.imports.all_sprites as s

class block_pm_numeric(block):
    def __init__(self, screen, stage, state_index, pos, number=-1):
        super().__init__(screen, stage, state_index, pos)
        self.number = 0
        self.options(str(number))
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_pm_numeric(self.screen, self.stage, new_state_index, self.pos, self.number)

    def replaced_with(self):
        if self.number > 1:
            return block_pm_numeric(self.screen, self.stage, self.state_index, self.pos, self.number-1)
        else:
            return block_empty(self.screen, self.stage, self.state_index, self.pos)

    def on_step_out(self):
        self.stage.states[self.state_index].set_block(self.pos, self.replaced_with())

    def options(self, option):
        self.number = int(option[-1]) - int('0')
        if 1 <= self.number <= 8:
            self.sprite = s.sprites["block_numeric_" + str(self.number) + "_pm"]
        else:
            self.sprite = s.sprites["error"]
