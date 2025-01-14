import src.imports.utils as u
import src.imports.globals as g
from src.animations.animation_spinning_dog import animation_spinning_dog
from src.blocks.pure.block_perma import block_perma
from resources.strings.translation_getters import get_message_strings

MS = get_message_strings(g.save_state.get_language())


class block_cycle_detector(block_perma):
    def __init__(self, screen, stage, state_index, pos, cycle_count=0, player_out_direction=None):
        super().__init__(screen, stage, state_index, pos)
        self.player_out_direction = player_out_direction
        self.cycle_count = cycle_count

    def on_step_out(self):
        self.player_out_direction = self.stage.states[self.state_index].player.this_move_direction

    def on_step_in(self):
        if self.player_out_direction is None:
            return
        if self.player_out_direction != u.reverse_direction(
                self.stage.states[self.state_index].player.last_move_direction):
            # cycle detected
            self.cycle_count += 1
            match self.cycle_count:
                case 5:
                    self.stage.animation_manager.register_message(self.screen, MS.loops_5, -1)
                case 10:
                    self.stage.animation_manager.register_message(self.screen, MS.loops_10, -1)
                case 15:
                    self.stage.animation_manager.register_message(self.screen, MS.loops_15, -1)
                case 20:
                    self.stage.animation_manager.register_message(self.screen, MS.loops_20, -1)
                case 23:
                    self.stage.animation_manager.register_message(self.screen, MS.dog_infestation, -1)
                    for _ in range(23):
                        self.stage.animation_manager.register_animation(animation_spinning_dog(self.screen))
            if self.cycle_count > 23:
                self.stage.animation_manager.register_animation(animation_spinning_dog(self.screen))

    def copy(self, new_state_index):
        return block_cycle_detector(self.screen, self.stage, new_state_index, self.pos, self.cycle_count,
                                    self.player_out_direction)
