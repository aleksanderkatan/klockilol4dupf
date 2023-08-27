import queue

import src.imports.all_sprites as s
import src.imports.utils as u
from src.blocks.block import block
from src.blocks.pure.block_blocker import block_blocker
from src.blocks.semi_pure.block_dummy import block_dummy
from src.blocks.block_empty import block_empty
from src.blocks.impure.block_invisible import block_invisible
from src.blocks.semi_pure.block_lamp import block_lamp
from src.blocks.semi_pure.block_moving_arrow import block_moving_arrow
from src.blocks.pure.block_numeric import block_numeric
from src.blocks.pure.block_piston import block_piston
from src.blocks.semi_pure.block_swapping_trigger import block_swapping_trigger
from src.imports.view_constants import global_view_constants as v
from src.logic.direction import direction as d


class block_thunder(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_thunder"]

    def copy(self, new_state_index):
        return block_thunder(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.player.enqueue_move(d.FORCED_SKIP)  # !! just in case
        array = [[0] * state.y for i in range(state.x)]
        Q = queue.Queue()
        px, py, pz = self.pos
        Q.put((px, py))

        shifts = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        while not Q.empty():
            x, y = Q.get()
            for shift in shifts:
                sx, sy = shift
                nx = x + sx
                ny = y + sy
                if u.out_of_range(nx, ny, state.x, state.y):
                    continue
                if array[nx][ny] != 0:
                    continue
                if type(state.get_block((nx, ny, pz))) not in [block_empty, block_invisible, block_blocker]:
                    Q.put((nx, ny))
                    array[nx][ny] = 1

        for i in range(state.x):
            for j in range(state.y):
                if array[i][j] == 1:
                    trigger = False
                    if type(state.get_block((i, j, pz))) in [block_dummy, block_lamp, block_numeric,
                                                             block_moving_arrow]:
                        state.get_block((i, j, pz)).on_step_out()
                        trigger = True
                    if type(state.get_block((i, j, pz))) in [block_piston, block_swapping_trigger]:
                        state.get_block((i, j, pz)).on_step_in()
                        trigger = True
                    if trigger:
                        x, y = u.index_to_position(i, j, pz, state.x, state.y, state.z, True)
                        self.stage.particle_generator.generate_dust(v.THUNDER_PARTICLES, (x, y))
