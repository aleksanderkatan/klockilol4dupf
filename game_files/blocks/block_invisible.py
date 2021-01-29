from game_files.blocks.block import block
import game_files.all_sprites as s

class block_invisible(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)

    def copy(self, new_state_index):
        return block_invisible(self.screen, self.stage, new_state_index, self.pos)

    def draw(self, pos, where_is_player):
        pass
