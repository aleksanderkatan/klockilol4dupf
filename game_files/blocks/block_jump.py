from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.all_sprites as s

class block_jump(block):
    def __init__(self, screen, stage, state_index, pos, boost=-1):
        super().__init__(screen, stage, state_index, pos)
        self.set_boost(boost)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_jump(self.screen, self.stage, new_state_index, self.pos, self.boost)

    def on_step_in(self):
        self.stage.states[self.state_index].player.boost_next_move(self.boost)

    def set_boost(self, boost):
        self.boost = boost
        if 2 <= boost <= 3:
            self.sprite = s.sprites["block_jump_" + str(boost)]
        else:
            self.sprite = s.sprites["error"]
