import src.imports.all_sprites as s
from src.blocks.block import block
from src.blocks.platform_maze.block_pm_triggerable_off import block_pm_triggerable_off
from src.blocks.platform_maze.block_pm_triggerable_on import block_pm_triggerable_on


class block_pm_triggerer(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pm_triggerer"]

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        for blo in state.block_iterator():
            if issubclass(type(blo), block_pm_triggerable_off):
                state.set_block(blo.pos, block_pm_triggerable_on(self.screen, self.stage, self.state_index, blo.pos))

    def copy(self, new_state_index):
        return block_pm_triggerer(self.screen, self.stage, new_state_index, self.pos)
