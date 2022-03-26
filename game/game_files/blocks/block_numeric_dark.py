from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.imports.all_sprites as s

d = {'X': 1, 'Y': 2, 'Z': 3}
d1 = {1: 'X', 2: 'Y', 3: 'Z'}

class block_numeric_dark(block):
    def __init__(self, screen, stage, state_index, pos, visible=True, number=-1):
        super().__init__(screen, stage, state_index, pos)
        self.number = number
        self.visible = visible
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_numeric_dark(self.screen, self.stage, new_state_index, self.pos, self.visible, self.number)

    def replaced_with(self):
        if self.number > 1:
            return block_numeric_dark(self.screen, self.stage, self.state_index, self.pos, self.visible, self.number-1)
        else:
            return block_empty(self.screen, self.stage, self.state_index, self.pos)

    def on_step_out(self):
        self.stage.states[self.state_index].set_block(self.pos, self.replaced_with())

    def update_visibility(self):
        state = self.stage.states[self.state_index]
        player = state.player
        dist = 0
        for a, b in zip(player.pos, self.pos):
            dist = max(dist, abs(a-b))
        self.visible = state.dark_visibility >= dist
        self.evaluate_sprite()

    def evaluate_sprite(self):
        if not (1 <= self.number <= 3):
            self.sprite = s.sprites["error"]
            return
        if self.visible:
            self.sprite = s.sprites["block_numeric_" + str(self.number) + "_dark"]
        else:
            self.sprite = s.sprites["block_numeric_" + str(self.number) + "_invisible_dark"]

    def options(self, option):
        if option[0] not in d:
            self.number = -1
        else:
            self.number = d[option[0]]
        self.evaluate_sprite()
