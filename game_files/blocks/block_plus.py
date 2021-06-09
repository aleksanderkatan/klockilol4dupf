from game_files.blocks.block import block
import game_files.all_sprites as s

class block_plus(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_plus"]

    def copy(self, new_state_index):
        return block_plus(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.dark_visibility += 1
