from game_files.blocks.block import block
import game_files.imports.all_sprites as s


class block_lamp(block):
    def __init__(self, screen, stage, state_index, pos, on=False):
        super().__init__(screen, stage, state_index, pos)
        self.on = on
        self.sprite = self.evaluate_sprite(self.on)

    def copy(self, new_state_index):
        return block_lamp(self.screen, self.stage, new_state_index, self.pos, self.on)

    def on_step_out(self):
        self.change_state()

    def change_state(self):
        self.on = not self.on
        self.sprite = self.evaluate_sprite(self.on)

    def evaluate_sprite(self, on):
        # if on:
        #     return s.sprites["block_lamp_on"]
        # else:
        #     return s.sprites["block_lamp_off"]

        if on:
            return s.sprites["block_yellow"]
        else:
            return s.sprites["block_orange"]
