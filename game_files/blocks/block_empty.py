from game_files.blocks.block import block

class block_empty(block):
    def __init__(self, screen, stage, state_index, pos): # !! intentional
        pass

    def draw(self, pos, where_is_player):
        pass

    def copy(self, new_state_index):
        return self
