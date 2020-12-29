from objects.obj_block import block
import import_sprites as s

class block_start(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["obj_block_start"]

    def copy(self, new_state_index):
        return block_start(self.screen, self.stage, new_state_index, self.pos)
