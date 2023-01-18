from game_files.blocks.block import block
import game_files.imports.all_sprites as s
from game_files.imports.log import log
import game_files.imports.all_random_level_generators as r


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
        match self.configuration:
            case 1:
                # If it fails, it fails. It will log an error.
                r.generate_SISLG((201, 8))
            case None:
                log.warning("Ominous thing is None!")
            case _:
                log.warning(f"Unknown ominous thing: {self.configuration}, {type(self.configuration)}")

    def on_step_out(self):
        self.stage.change_to = None
