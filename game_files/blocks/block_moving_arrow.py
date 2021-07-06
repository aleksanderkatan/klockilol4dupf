from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.imports.all_sprites as s
import game_files.imports.utils as u

class block_moving_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=-1):
        super().__init__(screen, stage, state_index, pos)
        self.direction = -1
        self.sprite = s.sprites["error"]
        self.set_direction(direction)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_moving_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def on_step_out(self):
        old_pos = self.pos
        new_pos = u.move_pos(old_pos, self.direction)
        state = self.stage.states[self.state_index]
        swap_block = state.get_block(new_pos)
        if issubclass(type(swap_block), block_empty):
            state.set_block(old_pos, swap_block)
            state.set_block(new_pos, self)
        if swap_block is None:
            state.set_block(old_pos, block_empty(self.screen, self.stage, self.state_index, self.pos))

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_moving_arrow_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]
