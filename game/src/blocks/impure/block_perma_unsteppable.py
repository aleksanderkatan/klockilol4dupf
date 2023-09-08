from src.blocks.pure.block_perma import block_perma


class block_perma_unsteppable(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)

    def copy(self, new_state_index):
        return block_perma_unsteppable(self.screen, self.stage, new_state_index, self.pos)

    def has_barrier(self, direction, into):
        return into
