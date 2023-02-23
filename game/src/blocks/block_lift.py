import src.imports.all_blocks as o
import src.imports.all_sprites as s
from src.blocks.block import block
from src.logic.direction import direction as d


class block_lift(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites["block_orange"]

    def copy(self, new_state_index):
        return block_lift(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        target_z = self.pos[2] + 1
        bound_z = self.stage.states[self.state_index].get_size()[2]

        while target_z < bound_z:
            target_pos = (self.pos[0], self.pos[1], target_z)
            if type(self.stage.states[self.state_index].get_block(target_pos)) in o.standables:
                break
            target_z += 1

        if target_z < bound_z:
            player = self.stage.states[self.state_index].player
            player.enqueue_move(d.ASCEND)
            player.boost_next_move(target_z - self.pos[2])
            # self.stage.states[self.state_index].teleport_player((self.pos[0], self.pos[1], target_z))
