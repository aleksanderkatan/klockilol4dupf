from game_files.blocks.block import block
import game_files.all_blocks as o
import game_files.all_sprites as s

class block_portal(block):
    def __init__(self, screen, stage, state_index, pos, destination=None):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites["block_portal"]
        self.destination = destination

    def copy(self, new_state_index):
        return block_portal(self.screen, self.stage, new_state_index, self.pos, self.destination)

    def on_step_in(self):
        self.stage.states[self.state_index].teleport_player(self.destination.pos, activate_step_in=False)
        player = self.stage.states[self.state_index].player
        player.enqueue_move(player.last_move_direction)

    def set_destination(self, destination):
        self.destination = destination
