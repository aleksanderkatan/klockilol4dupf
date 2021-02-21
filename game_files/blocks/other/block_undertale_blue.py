from game_files.blocks.block import block
from game_files.blocks.other.block_undertale_yellow import block_undertale_yellow
import game_files.all_sprites as s

class block_undertale_blue(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_ice"]

    def copy(self, new_state_index):
        return block_undertale_blue(self.screen, self.stage, new_state_index, self.pos)

    def probe_for_yellow(self):
        x, y, z = self.pos
        offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for off in offset:
            nx = x+off[0]
            ny = y+off[1]
            blo = self.stage.latest_state().get_block((nx, ny, z))
            if type(blo) is block_undertale_yellow:
                return True
        return False

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        dir = player.last_move_direction

        if player.flavour == 1 or self.probe_for_yellow():
            if dir is not None and dir != 4:
                new_dir = dir + 2 * (1 if dir < 2 else -1)
                player.enqueue_move(new_dir)