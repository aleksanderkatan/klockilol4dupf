import source_code.imports.all_sprites as s
from source_code.blocks.block import block
from source_code.logic.direction import direction as d


class block_blocker(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_blocker"]
        self.direction = d.NONE

    def copy(self, new_state_index):
        return block_blocker(self.screen, self.stage, new_state_index, self.pos)
