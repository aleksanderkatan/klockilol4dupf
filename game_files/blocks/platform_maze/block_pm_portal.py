from game_files.blocks.block import block
import game_files.imports.all_sprites as s

class block_pm_portal(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites["block_pm_portal"]

    def copy(self, new_state_index):
        return block_pm_portal(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        destination = None
        for blo in state.block_iterator():
            if issubclass(type(blo), block_pm_portal) and blo != self:
                destination = blo
                break
        if destination is None:
            destination = self

        state.teleport_player(destination.pos, activate_step_in=False)
