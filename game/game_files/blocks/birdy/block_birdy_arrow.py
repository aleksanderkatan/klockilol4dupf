from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u
from game_files.logic.direction import direction as d


class block_birdy_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=d.NONE):
        super().__init__(screen, stage, state_index, pos)
        self.direction = direction
        self.sprite = s.sprites["error"]
        self.set_direction(direction)

    def set_direction(self, direction):
        self.direction = direction
        if direction.is_cardinal():
            self.sprite = s.sprites["block_birdy_arrow_" + str(direction.value)]
        else:
            self.sprite = s.sprites["error"]

    def copy(self, new_state_index):
        return block_birdy_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def has_barrier(self, direction, into):
        return direction == self.direction and into is True

