import src.imports.all_sprites as s
from src.blocks.block import block
from src.imports.log import log


class block_pm_flight(block):
    def __init__(self, screen, stage, state_index, pos, length=5):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pm_flight"]
        self.length = length

    def copy(self, new_state_index):
        return block_pm_flight(self.screen, self.stage, new_state_index, self.pos, self.length)

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        player.flight = self.length
        log.trace("flight!")
