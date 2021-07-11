from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.levels as l
from game_files.imports.view_constants import global_view_constants as v
from game_files.imports.save_state import global_save_state

class block_entrance(block):
    def __init__(self, screen, stage, state_index, pos, target_level=None):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.sprite_av = s.sprites["level_available"]
        self.sprite_unav = s.sprites["level_unavailable"]
        self.target_level = None
        self.set_target_level(target_level)

    def copy(self, new_state_index):
        return block_entrance(self.screen, self.stage, new_state_index, self.pos, self.target_level)

    def options(self, option):
        target_level = option.split('/')
        target_level = (int(target_level[0]), int(target_level[1]))
        self.set_target_level(target_level)

    def set_target_level(self, target_level):
        if target_level is None:
            return
        self.target_level = target_level
        if l.is_hub(target_level):
            self.sprite = s.sprites["block_entrance_hub"]
        if l.is_zone(target_level):
            self.sprite = s.sprites["block_entrance_zone"]
        if l.is_level(target_level):
            self.sprite = s.sprites["block_entrance_level"]

    def get_target_level(self):
        return self.target_level

    def on_step_in(self):
        if global_save_state.is_available(self.target_level):
            self.stage.change_to = self.target_level

    def on_step_out(self):
        self.stage.change_to = None

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            super().draw(pos, where_is_player)

            completion_pos = (pos[0]+v.LEVEL_COMPLETION_OFFSET, pos[1]+v.LEVEL_COMPLETION_OFFSET)

            if global_save_state.is_completed(self.target_level):
                self.screen.blit(self.sprite_av[where_is_player], completion_pos)
            elif global_save_state.is_available(self.target_level):
                pass
            else:
                self.screen.blit(self.sprite_unav[where_is_player], completion_pos)

