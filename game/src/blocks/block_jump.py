from src.blocks.block import block
import src.imports.all_sprites as s


class block_jump(block):
    def __init__(self, screen, stage, state_index, pos, boost=-1):
        super().__init__(screen, stage, state_index, pos)
        self.boost = 0
        self.options(str(boost))
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_jump(self.screen, self.stage, new_state_index, self.pos, self.boost)

    def on_step_in(self):
        self.stage.states[self.state_index].player.boost_next_move(self.boost)

    def options(self, option):
        self.boost = int(option)
        if 2 <= self.boost <= 3:
            self.sprite = s.sprites["block_jump_" + str(self.boost)]
        else:
            self.sprite = s.sprites["error"]
