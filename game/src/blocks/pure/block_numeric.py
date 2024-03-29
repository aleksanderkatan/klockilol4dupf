import random

import src.imports.all_sprites as s
import src.imports.globals as g
from src.animations.animation_disappearing_block import animation_disappearing_block
from src.blocks.block import block
from src.blocks.block_empty import block_empty


class block_numeric(block):
    def __init__(self, screen, stage, state_index, pos, number=-1):
        super().__init__(screen, stage, state_index, pos)
        self.number = 0
        self.options(str(number))
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_numeric(self.screen, self.stage, new_state_index, self.pos, self.number)

    def replaced_with(self):
        if self.number > 1:
            return block_numeric(self.screen, self.stage, self.state_index, self.pos, self.number - 1)
        else:
            return block_empty(self.screen, self.stage, self.state_index, self.pos)

    def on_step_out(self):
        state = self.stage.states[self.state_index]
        state.set_block(self.pos, self.replaced_with())

        if self.number == 1:
            if self.stage.level_index[0] == 209 or g.save_state.get_preference("disappearing_blocks"):
                if random.random() < 0.9999:
                    self.stage.animation_manager.register_animation(
                        animation_disappearing_block(self.screen, self.stage, self.state_index, self.sprite[0],
                                                     pos=self.pos)
                    )
                else:
                    # easter egg, sometimes blocks' animation in "platform maze" appeared in the screen corner
                    self.stage.animation_manager.register_animation(
                        animation_disappearing_block(self.screen, self.stage, self.state_index, self.sprite[0],
                                                     screen_pos=(0, 0))
                    )

    def options(self, option):
        self.number = int(option[-1]) - int('0')
        if 1 <= self.number <= 8:
            self.sprite = s.sprites["block_numeric_" + str(self.number)]
        else:
            self.sprite = s.sprites["error"]
