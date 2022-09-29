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
        dir = self.stage.states[self.state_index].player.last_move_direction

        old_pos = player.pos
        new_pos = u.move_pos(old_pos, dir, self.length)
        translation = u.get_translation(old_pos, new_pos)

        if dir.is_cardinal():
            self.stage.states[self.state_index].player.enqueue_move(dir)
        # self.stage.animation_manager.register_animation(animation_player_jump(self.screen, self.stage, self.state_index, translation))
