from game_files.blocks.block import block
import game_files.imports.utils as u
import game_files.imports.all_sprites as s


class block_dual_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction_1=-1, direction_2=-1):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["error"]
        self.direction_1 = -1
        self.direction_2 = -1
        self.set_directions(direction_1, direction_2)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_dual_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction_1, self.direction_2)

    def on_step_in(self):
        print(self.direction_1, self.direction_2)
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

        if self.direction_1 not in range(4) or self.direction_2 not in range(4):
            self.sprite = s.sprites["error"]
            return

        if not ((self.direction_1 + 1 == self.direction_2) or (self.direction_1 == 0 and self.direction_2 == 3)):
            self.sprite = s.sprites["error"]
            return

        if self.direction_1 == 0 and self.direction_2 == 3:
            self.sprite = s.sprites["block_dual_arrow_3"]
        else:
            self.sprite = s.sprites["block_dual_arrow_" + str(self.direction_1)]

    def has_barrier(self, direction, into):
        barrier_directions = [i for i in range(4) if i not in [self.direction_1, self.direction_2]]
        return direction in barrier_directions
