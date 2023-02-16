from src.blocks.block import block
import src.imports.all_sprites as s
from src.imports.log import log


class block_pm_control_switcher(block):
    def __init__(self, screen, stage, state_index, pos, reverses=True):
        super().__init__(screen, stage, state_index, pos)
        self.reverses = True
        self.sprite = s.sprites["error"]
        self.options("reverses" if reverses else "resets")

    def copy(self, new_state_index):
        return block_pm_control_switcher(self.screen, self.stage, new_state_index, self.pos, self.reverses)

    def options(self, option):
        self.reverses = option == "reverses"
        if self.reverses:
            self.sprite = s.sprites["block_pm_control_switcher_switch"]
        else:
            self.sprite = s.sprites["block_pm_control_switcher_reset"]

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        log.trace(f"Player controls are reversed: {self.reverses}")
        player.switched_controls = self.reverses
