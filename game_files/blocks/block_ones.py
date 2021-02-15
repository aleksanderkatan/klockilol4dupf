from game_files.blocks.block import block
import game_files.all_sprites as s
from game_files.all_blocks import block_numeric


class block_ones(block):
    def __init__(self, screen, stage, state_index, pos, ones=None):
        super().__init__(screen, stage, state_index, pos)

        if ones is None:
            self.ones = [True, True, True, True]
        else:
            self.ones = []
            for i in range(4):
                self.ones.append(ones[i])
        self.sprite = s.sprites["block_ones"]

    def copy(self, new_state_index):
        return block_ones(self.screen, self.stage, new_state_index, self.pos, self.ones)

    def on_step_in(self):
        x, y, z = self.pos
        poses = [(x + 1, y, z), (x, y - 1, z), (x - 1, y, z), (x, y + 1, z)]
        for i in range(4):
            if self.ones[i]:
                self.stage.states[self.state_index].set_block(
                    poses[i], block_numeric(self.screen, self.stage, self.state_index, poses[i], 1)
                )

    def options(self, option):
        if option.find("1") >= 0:
            val = int(option)
            self.ones = [val // 1000 == 1, (val % 1000) // 100 == 1, (val % 100) // 10 == 1, (val % 10) == 1]
        else:
            self.ones = [option.find(">") >= 0, option.find("^") >= 0, option.find("<") >= 0, option.find("v") >= 0]

    def draw(self, pos, where_is_player):
        super().draw(pos, where_is_player)
        if where_is_player is not None:
            for i in range(4):
                if self.ones[i]:
                    self.screen.blit(s.sprites["ones_one_" + str(i)][where_is_player], pos)
