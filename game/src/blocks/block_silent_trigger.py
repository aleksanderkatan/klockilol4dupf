from src.blocks.block import block
import src.imports.all_sprites as s
from src.imports.log import log
import src.imports.all_random_level_generators as r
from src.level_generators.spelunky_inspired_segmented_level_generator.all_5x5_segments import *


class block_silent_trigger(block):
    def __init__(self, screen, stage, state_index, pos, configuration=None):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]
        self.configuration = configuration

    def copy(self, new_state_index):
        return block_silent_trigger(self.screen, self.stage, new_state_index, self.pos, self.configuration)

    def options(self, option):
        self.configuration = int(option)

    def on_step_in(self):
        success = False
        match self.configuration:
            case 1:
                success = r.generate_SISLG((201, 7), preset_hard_numeric, 4, 3)
            case 2:
                success = r.generate_SISLG((201, 8), preset_harder, 4, 3)
            case None:
                log.warning("Ominous thing is None!")
            case _:
                log.warning(f"Unknown ominous thing: {self.configuration}, {type(self.configuration)}")

        if success:
            log.info("SUCCESS: something ominous happened")
        else:
            log.error(f"FAIL: something ominous failed to happen.")

    def on_step_out(self):
        self.stage.change_to = None
