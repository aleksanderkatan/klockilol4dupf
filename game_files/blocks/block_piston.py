from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.utils as u
import game_files.all_sprites as s

class pusher:
    def __init__(self, screen, stage, state_index, pos, direction):
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.pos = pos
        self.direction = direction
        self.clinged = False
        self.finished = False
        self.sprite = s.sprites["pusher_" + str(self.direction)]

    def move(self):
        if self.finished:
            return

        ox, oy, z = self.pos
        shifts = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        dx, dy = shifts[self.direction]
        nx = ox+dx
        ny = oy+dy

        state = self.stage.states[self.state_index]
        if self.clinged is False:
            if u.out_of_range(nx, ny, state.x, state.y):
                self.finished = True
                self.pos = (nx, ny, z)
            else:
                blo = state.get_block((nx, ny, z))
                if type(blo) is not block_empty:
                    self.clinged = True
        else:
            if u.out_of_range(nx, ny, state.x, state.y):
                state.set_block((ox, oy, z), block_empty(self.screen, self.stage, self.state_index, (nx, ny, z)))
                self.finished = True
            else:
                temp = state.get_block((nx, ny, z))
                if type(temp) is block_empty:
                    state.set_block((nx, ny, z), state.get_block((ox, oy, z)))
                    state.set_block((ox, oy, z), temp)

                    state.get_block((nx, ny, z)).pos = (nx, ny, z)
                    state.get_block((ox, oy, z)).pos = (ox, oy, z)
                else:
                    self.finished = True

        if state.player.pos == (ox, oy, z) and self.clinged:
            if self.finished:
                state.player.enqueue_move(self.direction)
            else:
                state.teleport_player((nx, ny, z), False)
        self.pos = (nx, ny, z)

    def draw(self, pos):
        self.screen.blit(self.sprite[0], pos)

    def copy(self, new_state_index):
        res = pusher(self.screen, self.stage, new_state_index, self.pos, self.direction)
        res.clinged = self.clinged
        res.finished = self.finished
        res.sprite = self.sprite
        return res

class block_piston(block):
    def __init__(self, screen, stage, state_index, pos, direction=-1):
        super().__init__(screen, stage, state_index, pos)
        self.direction = -1
        self.set_direction(direction)
        self.state_index = state_index

    def copy(self, new_state_index):
        return block_piston(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def on_step_out(self):
        self.stage.states[self.state_index].pushers.append(
            pusher(self.screen, self.stage, self.state_index, self.pos, self.direction)
        )
        player = self.stage.states[self.state_index].player
        if player.pos == self.pos:
            player.enqueue_move(None)

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_piston_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]
