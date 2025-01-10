import src.imports.utils as u
from src.blocks.pure.block_perma import block_perma


class block_cycle_detector(block_perma):
    def __init__(self, screen, stage, state_index, pos, cycle_count=0, player_out_direction=None):
        super().__init__(screen, stage, state_index, pos)
        self.player_out_direction = player_out_direction
        self.cycle_count = cycle_count

    def on_step_out(self):
        self.player_out_direction = self.stage.states[self.state_index].player.this_move_direction

    def on_step_in(self):
        if self.player_out_direction is None:
            return
        if self.player_out_direction != u.reverse_direction(self.stage.states[self.state_index].player.last_move_direction):
            # cycle detected
            self.cycle_count += 1
            if self.cycle_count == 2:
                print("Goal achieved")


    def copy(self, new_state_index):
        return block_cycle_detector(self.screen, self.stage, new_state_index, self.pos, self.cycle_count, self.player_out_direction)

