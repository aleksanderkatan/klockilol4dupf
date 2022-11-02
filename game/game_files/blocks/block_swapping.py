from game_files.blocks.block import block
import game_files.imports.all_sprites as s


def evaluate_sprite(on):
    if on:
        return s.sprites["block_map_bridge_on"]
    else:
        return s.sprites["block_map_bridge_off"]


class block_swapping(block):
    def __init__(self, screen, stage, state_index, pos, on=False):
        super().__init__(screen, stage, state_index, pos)
        self.on = on
        self.sprite = evaluate_sprite(self.on)

    def copy(self, new_state_index):
        return block_swapping(self.screen, self.stage, new_state_index, self.pos, self.on)

    def set_state(self, state):
        self.on = state
        self.sprite = evaluate_sprite(self.on)

    def change_state(self):
        self.set_state(not self.on)

    def on_step_in(self):
        if not self.on:
            player = self.stage.states[self.state_index].player
            player.dead = True

    # def on_step_out(self):
    #     if self.on:
    #         self.change_state()

    def options(self, option):
        if option == "Q":
            self.set_state(True)
        elif option == "q":
            self.set_state(False)
