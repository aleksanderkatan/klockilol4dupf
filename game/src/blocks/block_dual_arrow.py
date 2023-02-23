import src.imports.all_sprites as s
import src.imports.utils as u
from src.blocks.block import block
from src.logic.direction import direction as d
from src.logic.direction import get_cardinal


class block_dual_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction_1=d.NONE, direction_2=d.NONE):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.direction_1 = d.NONE
        self.direction_2 = d.NONE
        self.set_directions(direction_1, direction_2)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_dual_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction_1, self.direction_2)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        if state.player.last_move_direction == u.reverse_direction(self.direction_1):
            state.player.enqueue_move(self.direction_2)
        elif state.player.last_move_direction == u.reverse_direction(self.direction_2):
            state.player.enqueue_move(self.direction_1)

    def options(self, option):
        direction_1 = u.char_to_direction(option[0])
        direction_2 = u.char_to_direction(option[1])
        self.set_directions(direction_1, direction_2)

    def set_directions(self, direction_1, direction_2):
        self.direction_1 = min(direction_1, direction_2)
        self.direction_2 = max(direction_1, direction_2)

        if not self.direction_1.is_cardinal() or not self.direction_2.is_cardinal():
            self.sprite = s.sprites["error"]
            return

        if not ((self.direction_1.value + 1 == self.direction_2.value) or (
                self.direction_1.value == 0 and self.direction_2.value == 3)):
            self.sprite = s.sprites["error"]
            return

        if self.direction_1 == d.RIGHT and self.direction_2 == d.DOWN:
            self.sprite = s.sprites["block_dual_arrow_3"]
        else:
            self.sprite = s.sprites["block_dual_arrow_" + str(self.direction_1.value)]

    def has_barrier(self, direction, into):
        barrier_directions = [dir for dir in get_cardinal() if dir not in [self.direction_1, self.direction_2]]
        return direction in barrier_directions
