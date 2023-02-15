from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u
from game_files.imports.view_constants import global_view_constants as v


class block_portal(block):
    def __init__(self, screen, stage, state_index, pos, destination_index=None, my_index=None):
        super().__init__(screen, stage, state_index, pos)
        self.state_index = state_index
        self.sprite = s.sprites["block_lift"]
        self.destination_index = destination_index
        self.my_index = my_index

    def copy(self, new_state_index):
        return block_portal(self.screen, self.stage, new_state_index, self.pos, self.destination_index, self.my_index)

    def on_step_in(self):
        state = self.stage.states[self.state_index]
        destination = state.find_portal(self.destination_index)
        if destination is None:
            destination = self

        state.teleport_player(destination.pos, activate_step_in=False)
        player = state.player
        if player.last_move_direction.is_cardinal():
            player.enqueue_move(player.last_move_direction)
        # particles
        old_x, old_y = u.index_to_position(self.pos[0], self.pos[1], self.pos[2], state.x, state.y, state.z, True)
        new_x, new_y = u.index_to_position(destination.pos[0], destination.pos[1], destination.pos[2],
                                           state.x, state.y, state.z, True)
        self.stage.particle_generator.generate_stars(v.PORTAL_PARTICLES, (old_x, old_y))
        self.stage.particle_generator.generate_stars(v.PORTAL_PARTICLES, (new_x, new_y))

    def options(self, option):
        o = option.split()
        self.destination_index = int(o[1])
        self.my_index = int(o[0])
