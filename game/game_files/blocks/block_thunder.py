from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
from game_files.blocks.block_invisible import block_invisible
from game_files.blocks.block_blocker import block_blocker

from game_files.blocks.block_dummy import block_dummy
from game_files.blocks.block_lamp import block_lamp
from game_files.blocks.block_numeric import block_numeric
from game_files.blocks.block_piston import block_piston
from game_files.blocks.block_moving_arrow import block_moving_arrow
from game_files.blocks.block_swapping_trigger import block_swapping_trigger
import game_files.imports.all_sprites as s
import queue
import game_files.imports.utils as u
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v

class block_thunder(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_thunder"]

    def copy(self, new_state_index):
        return block_thunder(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        state.player.enqueue_move(5)     # !!
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
                    if type(state.get_block((i, j, pz))) in [block_dummy, block_lamp, block_numeric, block_moving_arrow]:
                        state.get_block((i, j, pz)).on_step_out()
                        trigger = True
                    if type(state.get_block((i, j, pz))) in [block_piston, block_swapping_trigger]:
                        state.get_block((i, j, pz)).on_step_in()
                        trigger = True
                    if trigger:
                        x, y = u.index_to_position(i, j, pz, state.x, state.y, len(state.layers))
                        self.stage.particle_generator.generate_dust(g.THUNDER_PARTICLES, (x+v.BLOCK_X_SIZE//2, y+v.BLOCK_Y_SIZE//2))

