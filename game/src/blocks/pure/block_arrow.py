import src.imports.all_sprites as s
import src.imports.utils as u
from src.blocks.block import block
from src.logic.direction import direction as d


class block_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=d.NONE):
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
        if direction.is_cardinal():
            self.sprite = s.sprites["block_arrow_" + str(direction.value)]
        else:
            self.sprite = s.sprites["error"]
