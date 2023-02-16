from src.blocks.block import block
import src.imports.all_sprites as s
import src.imports.all_blocks as o
from src.imports.log import log


def prevents_win(block):
    if issubclass(type(block), o.block_numeric):
        return True
    if issubclass(type(block), o.block_lamp):
        return not block.on
    if issubclass(type(block), o.block_numeric_dark):
        return block.visible
    return False


class block_end(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_end"]

    def copy(self, new_state_index):
        return block_end(self.screen, self.stage, new_state_index, self.pos)

    def perform_check(self):
        for lay in self.stage.states[self.state_index].layers:
            for row in lay.grid:
                for blo in row:
                    if prevents_win(blo):
                        return False
        return True

    def on_step_in(self):
        completed = self.perform_check()
        log.trace("Level completed check: " + str(completed))
        if completed:
            self.stage.states[self.state_index].completed = True
