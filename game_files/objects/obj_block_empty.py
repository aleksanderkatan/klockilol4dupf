from objects.obj_block import block

class block_empty(block):
    def draw(self, pos, where_is_player):
        pass

    def copy(self, new_state_index):
        return block_empty(self.screen, self.stage, new_state_index, self.pos)