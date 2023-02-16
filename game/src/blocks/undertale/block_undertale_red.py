from src.blocks.block import block
import src.imports.all_sprites as s


class block_undertale_red(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_thunder"]

    def copy(self, new_state_index):
        return block_undertale_red(self.screen, self.stage, new_state_index, self.pos)

    # def on_step_in(self):
    #     # self.stage.reverse()    # !! sketchy and doesn't work
    #     # self.stage.states[self.state_index].player.dead = True
    #     # player = self.stage.latest_state().player
    #     # self.stage.latest_state().teleport_player(player.last_move_pos)
    #     self.stage.states[self.state_index].invalid = True

    def has_barrier(self, direction, into):
        return True
