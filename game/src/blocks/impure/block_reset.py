import src.imports.all_sprites as s
from src.blocks.block import block


class block_reset(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_reset"]

    def copy(self, new_state_index):
        return block_reset(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        old_pos = self.stage.latest_state().player.pos
        self.stage.reset()
        self.stage.latest_state().teleport_player(old_pos, False)
