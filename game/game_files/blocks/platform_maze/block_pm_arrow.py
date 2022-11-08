from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u
from game_files.logic.direction import direction as d
from game_files.logic.direction import get_cardinal


class block_pm_arrow(block):
    def __init__(self, screen, stage, state_index, pos, directions=[]):
        super().__init__(screen, stage, state_index, pos)
        self.directions = directions
        self.barriers = []
        self.set_directions(directions)

    def copy(self, new_state_index):
        return block_pm_arrow(self.screen, self.stage, new_state_index, self.pos, self.directions)

    def on_step_in(self):
        pass

    def options(self, option):
        directions = [u.char_to_direction(elem) for elem in option]
        self.set_directions(directions)

    def set_directions(self, directions):
        self.sprite = s.sprites["error"]
        self.directions = directions
        if len(directions) == 1:  # single arrow
            if 0 <= directions[0].value <= 3:
                self.barriers = [dir for dir in get_cardinal() if dir != directions[0]]
                self.sprite = s.sprites["block_pm_arrow_" + str(directions[0].value)]
        if len(directions) == 2:  # double arrow
            if all(item in [d.RIGHT, d.LEFT] for item in directions):
                self.barriers = [d.UP, d.DOWN]
                self.sprite = s.sprites["block_pm_dual_arrow_0"]
            elif all(item in [d.UP, d.DOWN] for item in directions):
                self.barriers = [d.LEFT, d.RIGHT]
                self.sprite = s.sprites["block_pm_dual_arrow_1"]

    def has_barrier(self, direction, into):
        if into:
            return False
        return direction in self.barriers
