from game.game_files.blocks.block_perma import block_perma
import game.game_files.imports.all_sprites as s

class block_pm_triggerable_on(block_perma):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pm_triggerable_on"]

    def copy(self, new_state_index):
        return block_pm_triggerable_on(self.screen, self.stage, new_state_index, self.pos)
