from game_files.blocks.block import block
import game_files.imports.all_sprites as s
import game_files.imports.utils as u


class block_pm_jump(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_pm_jump"]
        self.length = 4

    def copy(self, new_state_index):
        return block_pm_jump(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        player = self.stage.states[self.state_index].player
        player.boost_next_move(self.length)
        dir = player.last_move_direction

        print(dir)
        print(dir.is_cardinal())

        if dir.is_cardinal():
            player.enqueue_move(dir)
            player.retain_direction_after_next_jump()
