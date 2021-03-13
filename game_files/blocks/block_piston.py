from game_files.blocks.block import block
from game_files.blocks.block_empty import block_empty
import game_files.utils as u
import game_files.all_sprites as s


class pusher:  # !! while pushers exist, on_step_ins are not called
    def __init__(self, screen, stage, state_index, pos, direction):
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.pos = pos
        self.direction = direction
        self.clinged = False
        self.finished = False
        self.sprite = s.sprites["pusher_" + str(self.direction)]
        self.first_move = True

    def move(self):
        if self.first_move:
            state = self.stage.states[self.state_index]
            blo = state.get_block(self.pos)
            if type(blo) is not block_empty:
                self.clinged = True
                if state.player.pos == self.pos and self.clinged and self.first_move:
                    state.get_block(self.pos).on_step_in()
            self.first_move = False


        if self.finished:
            return

        old_pos = self.pos
        new_pos = u.move_pos(self.pos, self.direction, 1)

        state = self.stage.states[self.state_index]

        if self.clinged is False:
            if u.out_of_range(new_pos[0], new_pos[1], state.x, state.y):
                self.finished = True
                self.pos = new_pos
            else:
                blo = state.get_block(new_pos)
                if type(blo) is not block_empty:
                    self.clinged = True
        else:
            if u.out_of_range(new_pos[0], new_pos[1], state.x, state.y):
                state.set_block(old_pos, block_empty(self.screen, self.stage, self.state_index, new_pos))
                self.finished = True
            else:
                temp = state.get_block(new_pos)
                if type(temp) is block_empty:
                    state.set_block(new_pos, state.get_block(old_pos))
                    state.set_block(old_pos, temp)

                    state.get_block(new_pos).pos = new_pos
                    state.get_block(old_pos).pos = old_pos
                else:
                    self.finished = True

        if state.player.pos == old_pos and self.clinged and state.player.enqueued_move is None:
            state.teleport_player(new_pos, False)

        if state.player.pos == old_pos and self.clinged and state.player.enqueued_move is None:
            if self.finished:
                state.get_block(old_pos).on_step_out()
                print('out')

        self.pos = new_pos

    def draw(self, pos):
        self.screen.blit(self.sprite[0], pos)

    def copy(self, new_state_index):
        res = pusher(self.screen, self.stage, new_state_index, self.pos, self.direction)
        res.clinged = self.clinged
        res.finished = self.finished
        res.first_move = self.first_move
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
        pos = u.move_pos(self.pos, self.direction, 1)
        my_pusher = pusher(self.screen, self.stage, self.state_index, pos, self.direction)
        self.stage.states[self.state_index].pushers.append(my_pusher)

        player = self.stage.states[self.state_index].player
        if player.pos == self.pos:
            player.enqueue_move(5)

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_piston_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]
