from game_files.blocks.block import block
import game_files.imports.utils as u
import game_files.imports.all_sprites as s

class block_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=-1):
        super().__init__(screen, stage, state_index, pos)
        self.direction = -1
        self.sprite = s.sprites["error"]
        self.set_direction(direction)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def on_step_in(self):
        self.stage.states[self.state_index].player.enqueue_move(self.direction)

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_arrow_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]
