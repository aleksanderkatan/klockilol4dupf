from game_files.blocks.block_perma import block_perma
import game_files.imports.all_sprites as s

class block_perma_unsteppable(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)

    def copy(self, new_state_index):
        return block_perma_unsteppable(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.invalid = True


