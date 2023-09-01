import src.imports.all_sprites as s
import src.imports.globals as g
import src.imports.levels as l
from src.blocks.block import block
from src.imports.view_constants import global_view_constants as v


status_sprites = {
    l.level_status.UNAVAILABLE: s.sprites["level_unavailable"],
    l.level_status.AVAILABLE: None,
    l.level_status.SKIPPED: s.sprites["level_skipped"],
    l.level_status.COMPLETED: s.sprites["level_completed"],
}


class block_entrance(block):
    def __init__(self, screen, stage, state_index, pos, target_level=(0, 0)):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.target_level = None
        self.set_target_level(target_level)

    def copy(self, new_state_index):
        return block_entrance(self.screen, self.stage, new_state_index, self.pos, self.target_level)

    def options(self, option):
        target_level = option.split('/')
        target_level = (int(target_level[0]), int(target_level[1]))
        self.set_target_level(target_level)

    def set_target_level(self, target_level):
        my_level = self.stage.level_index
        self.target_level = target_level
        if None in [target_level, my_level]:
            return

        if my_level[0] == 206 or target_level[0] == 206:
            self.sprite = s.sprites["block_entrance_hub"]
            return
        if l.is_level(target_level) or l.is_level(my_level):
            self.sprite = s.sprites["block_entrance_level"]
            return
        if l.is_zone(target_level) or l.is_zone(my_level):
            self.sprite = s.sprites["block_entrance_zone"]
            return
        if l.is_hub(target_level) or l.is_hub(my_level):
            self.sprite = s.sprites["block_entrance_hub"]
            return

    def get_target_level(self):
        return self.target_level

    def on_step_in(self):
        status = g.save_state.get_level_status(level_index=self.target_level)
        if status != l.level_status.UNAVAILABLE:
            self.stage.change_to = self.target_level

    def on_step_out(self):
        self.stage.change_to = None

    def draw(self, pos, where_is_player):
        super().draw(pos, where_is_player)
        if where_is_player is not None:
            completion_pos = (pos[0] + v.LEVEL_COMPLETION_OFFSET, pos[1] + v.LEVEL_COMPLETION_OFFSET)

            # for birdy and PM, 1st level acts as an entrance to the entire zone
            if self.target_level[0] in [205, 209]:
                return
            status = g.save_state.get_level_status(level_index=self.target_level)
            sprite = status_sprites[status]
            if sprite is not None:
                self.screen.blit(sprite[where_is_player], completion_pos)
