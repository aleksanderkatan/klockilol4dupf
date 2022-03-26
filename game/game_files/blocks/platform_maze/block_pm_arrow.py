from game.game_files.blocks.block import block
import game.game_files.imports.all_sprites as s
import game.game_files.imports.utils as u


class block_pm_arrow(block):
    def __init__(self, screen, stage, state_index, pos, directions=None):
        super().__init__(screen, stage, state_index, pos)
        if directions is None:
            directions = []
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
            if 0 <= directions[0] <= 3:
                self.barriers = [i for i in range(4) if i != directions[0]]
                self.sprite = s.sprites["block_pm_arrow_" + str(directions[0])]
        if len(directions) == 2:    # double arrow
            if all(item in [0, 2] for item in directions):
                self.barriers = [1, 3]
                self.sprite = s.sprites["block_pm_dual_arrow_0"]
            elif all(item in [1, 3] for item in directions):
                self.barriers = [0, 2]
                self.sprite = s.sprites["block_pm_dual_arrow_1"]

    def has_barrier(self, direction, into):
        if into:
            return False
        return direction in self.barriers
