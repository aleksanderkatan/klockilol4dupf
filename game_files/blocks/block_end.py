from blocks.block import block
import all_sprites as s
import utils as u
import levels as l

class block_end(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_end"]

    def copy(self, new_state_index):
        return block_end(self.screen, self.stage, new_state_index, self.pos)

    def perform_check(self):
        for lay in self.stage.states[self.state_index].layers:
            for row in lay.grid:
                for blo in row:
                    if u.prevents_win(blo):
                        return False
        return True

    def on_step_in(self):
        completed = self.perform_check()
        print("Level completed:", completed)
        if completed:
            self.stage.states[self.state_index].completed = True
