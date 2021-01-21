from game_files.blocks.block import block
import game_files.all_sprites as s
import game_files.utils as u
from game_files.save_state import global_save_state

class block_map_bridge(block):
    def __init__(self, screen, stage, state_index, pos, level_set=None):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.set_level_set(level_set)

    def copy(self, new_state_index):
        return block_map_bridge(self.screen, self.stage, new_state_index, self.pos, self.level_set)

    def on_step_in(self):
        if not global_save_state.is_set_completed(self.level_set):
            self.stage.states[self.state_index].player.dead = True

    def set_level_set(self, level_set):
        self.level_set = level_set
        if level_set is None:
            self.sprite = s.sprites["error"]
            return

        if global_save_state.is_set_completed(level_set):
            self.sprite = s.sprites["block_map_bridge_on"]
        else:
            self.sprite = s.sprites["block_map_bridge_off"]
