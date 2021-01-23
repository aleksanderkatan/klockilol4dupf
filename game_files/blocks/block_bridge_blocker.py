from game_files.blocks.block import block
import game_files.all_sprites as s
import game_files.utils as u

class block_bridge_blocker(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_bridge_blocker"]
        self.direction = None

    def copy(self, new_state_index):
        return block_bridge_blocker(self.screen, self.stage, new_state_index, self.pos)
