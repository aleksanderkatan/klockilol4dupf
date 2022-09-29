from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u

class block_undertale_yellow(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_yellow"]

    def copy(self, new_state_index):
        return block_undertale_yellow(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        dir = player.last_move_direction
        if dir.is_cardinal():
            new_dir = u.reverse_direction(dir)
            player.enqueue_move(new_dir)
