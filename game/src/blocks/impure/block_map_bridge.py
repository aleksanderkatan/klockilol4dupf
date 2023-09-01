import src.imports.all_sprites as s
import src.imports.globals as g
from src.blocks.block import block
import src.imports.levels as l

status_sprites = {
    l.level_status.UNAVAILABLE: s.sprites["block_map_bridge_off"],
    l.level_status.SKIPPED: s.sprites["block_map_bridge_skip"],
    l.level_status.COMPLETED: s.sprites["block_map_bridge_on"],
}


class block_map_bridge(block):
    def __init__(self, screen, stage, state_index, pos, level_set=None, allows_skip=True):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.level_set = level_set
        self.allows_skip = allows_skip
        self.set_level_set(level_set)

    def copy(self, new_state_index):
        return block_map_bridge(self.screen, self.stage, new_state_index, self.pos, self.level_set, self.allows_skip)

    def on_step_in(self):
        status = g.save_state.get_set_status(self.level_set)
        if status == l.level_status.UNAVAILABLE \
                or not self.allows_skip and status == l.level_status.SKIPPED:
            self.stage.states[self.state_index].player.dead = True

    # def has_barrier(self, direction, into):
    #     return not g.save_state.is_set_completed(self.level_set)

    def options(self, option):
        if option[-1] == "N":
            self.allows_skip = False
            self.set_level_set(int(option[:-1]))
        else:
            self.set_level_set(int(option))

    def set_level_set(self, level_set):
        self.level_set = level_set
        if level_set is None:
            self.sprite = s.sprites["error"]
            return

        self.sprite = status_sprites[g.save_state.get_set_status(level_set)]
