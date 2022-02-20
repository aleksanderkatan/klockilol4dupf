from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u
from game_files.animations.animation_player_jump import animation_player_jump

class block_pm_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=-1):
        super().__init__(screen, stage, state_index, pos)
        self.set_direction(direction)

    def copy(self, new_state_index):
        return block_pm_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.invalid_moves = [i for i in range(6) if i != self.direction]

    def options(self, option):
        direction = u.char_to_direction(option[0])
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_pm_arrow_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]

