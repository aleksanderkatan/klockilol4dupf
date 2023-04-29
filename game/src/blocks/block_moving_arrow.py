import src.imports.all_sprites as s
import src.imports.utils as u
from src.blocks.block import block
from src.blocks.block_empty import block_empty
from src.imports.view_constants import global_view_constants as v
from src.logic.direction import direction as d


class block_moving_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=d.NONE):
        super().__init__(screen, stage, state_index, pos)
        self.direction = -1
        self.sprite = s.sprites["error"]
        self.set_direction(direction)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_moving_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def on_step_out(self):
        old_pos = self.pos
        new_pos = u.move_pos(old_pos, self.direction)
        state = self.stage.states[self.state_index]
        swap_block = state.get_block(new_pos)
        if issubclass(type(swap_block), block_empty):
            state.set_block(old_pos, swap_block)
            state.set_block(new_pos, self)
        if swap_block is None:
            state.set_block(old_pos, block_empty(self.screen, self.stage, self.state_index, self.pos))
            x, y = u.index_to_position(old_pos[0], old_pos[1], old_pos[2], state.x, state.y, state.z, True)
            self.stage.particle_generator.generate_dust(v.THUNDER_PARTICLES, (x, y))

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def set_direction(self, direction):
        self.direction = direction
        if direction.is_cardinal():
            self.sprite = s.sprites["block_moving_arrow_" + str(direction.value)]
        else:
            self.sprite = s.sprites["error"]
