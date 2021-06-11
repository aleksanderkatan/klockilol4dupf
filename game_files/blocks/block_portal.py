from game_files.blocks.block import block
import game_files.imports.all_sprites as s

class block_portal(block):
    def __init__(self, screen, stage, state_index, pos, destination_index=None, my_index=None):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites["block_portal"]
        self.destination_index = destination_index
        self.my_index = my_index

    def copy(self, new_state_index):
        return block_portal(self.screen, self.stage, new_state_index, self.pos, self.destination_index, self.my_index)

    def on_step_in(self):
        destination = self.stage.states[self.state_index].find_portal(self.destination_index)
        if destination is None:
            destination = self

        self.stage.states[self.state_index].teleport_player(destination.pos, activate_step_in=False)
        player = self.stage.states[self.state_index].player
        if player.last_move_direction is not None and player.last_move_direction != 4:
            player.enqueue_move(player.last_move_direction)

    def options(self, option):
        o = option.split()
        self.destination_index = int(o[1])
        self.my_index = int(o[0])
