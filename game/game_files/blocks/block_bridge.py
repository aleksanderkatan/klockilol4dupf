from game_files.blocks.block import block
from game_files.blocks.block_blocker import block_blocker
import game_files.imports.all_sprites as s
import game_files.imports.utils as u

class block_bridge(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pink"]
        self.direction = None

    def copy(self, new_state_index):
        return block_bridge(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        self.direction = self.stage.states[self.state_index].player.last_move_direction
        dir = self.stage.states[self.state_index].player.last_move_direction
        if dir is not None and dir != 4:
            self.stage.states[self.state_index].player.enqueue_move(self.stage.states[self.state_index].player.last_move_direction)

    def on_step_out(self):
        sta = self.stage.states[self.state_index]
        direction = sta.player.this_move_direction

        if direction is None:
            return

        x, y, z = self.pos

        if direction == 0:
            x += 1
        elif direction == 1:
            y -= 1
        elif direction == 2:
            x -= 1
        elif direction == 3:
            y += 1

        if u.out_of_range(x, y, sta.x, sta.y):
            sta.player.dead = True
            return

        new_pos = (x, y, z)
        old_pos = self.pos

        state = self.stage.states[self.state_index]
        if not state.standable(new_pos):
            swap_block = state.get_block(new_pos)
            if type(swap_block) is block_blocker:
                return
            state.set_block(new_pos, self)
            state.set_block(old_pos, swap_block)
