from game_files.blocks.block import block
import game_files.imports.all_sprites as s

class block_ice(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_ice"]

    def copy(self, new_state_index):
        return block_ice(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        dir = self.stage.states[self.state_index].player.last_move_direction
        if dir.is_cardinal():
            self.stage.states[self.state_index].player.enqueue_move(dir)
