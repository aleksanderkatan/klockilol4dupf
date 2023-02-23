import src.imports.all_sprites as s
from src.blocks.block_perma import block_perma


class block_undertale_orange(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_orange"]

    def copy(self, new_state_index):
        return block_undertale_orange(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        player.flavour = 1
