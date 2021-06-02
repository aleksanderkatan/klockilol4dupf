from game_files.blocks.block import block
import game_files.all_sprites as s
import game_files.utils as u


class block_birdy_arrow(block):
    def __init__(self, screen, stage, state_index, pos, direction=-1):
        super().__init__(screen, stage, state_index, pos)
        self.direction = direction
        self.sprite = s.sprites["error"]
        self.set_direction(direction)

    def on_step_in(self):
        player = self.stage.latest_state().player
        if u.reverse_direction(player.last_move_direction) == self.direction:
            self.stage.states[self.state_index].invalid = True
            # self.stage.latest_state().teleport_player(player.last_move_pos)

    def set_direction(self, direction):
        self.direction = direction
        if 0 <= direction <= 3:
            self.sprite = s.sprites["block_birdy_arrow_" + str(direction)]
        else:
            self.sprite = s.sprites["error"]

    def copy(self, new_state_index):
        return block_birdy_arrow(self.screen, self.stage, new_state_index, self.pos, self.direction)

    def options(self, option):
        self.set_direction(u.char_to_direction(option[-1]))

