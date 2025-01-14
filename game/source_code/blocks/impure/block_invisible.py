import source_code.imports.all_sprites as s
from source_code.blocks.block import block


class block_invisible(block):
    def __init__(self, screen, stage, state_index, pos, discovered=False):
        super().__init__(screen, stage, state_index, pos)
        self.discovered = discovered

    def copy(self, new_state_index):
        return block_invisible(self.screen, self.stage, new_state_index, self.pos, self.discovered)

    def on_step_in(self):
        self.discovered = True

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            if not self.discovered:
                self.screen.blit(s.sprites["block_invisible"][0], pos)  # scaling visibility
            else:
                self.screen.blit(s.sprites["block_invisible_translucent"][0], pos)
