import src.imports.all_sprites as s
import src.imports.globals as g
from src.imports.view_constants import global_view_constants as v
from src.blocks.block import block
from src.animations.animation_jump import animation_jump
from src.animations.chained_animation import chained_animation


class block_madeline(block):
    def __init__(self, screen, stage, state_index, pos, has_madeline=True):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]
        self.has_madeline = has_madeline

    def copy(self, new_state_index):
        return block_madeline(self.screen, self.stage, new_state_index, self.pos, self.has_madeline)

    def on_step_in(self):
        if g.save_state.get("madeline_present", True):
            x, y, z = self.pos
            madeline_sprite = s.sprites["decoration_1x1_madeline"][0]
            madeline_blue_sprite = s.sprites["decoration_1x1_madeline_blue"][0]

            jump = animation_jump(self.screen, self.stage, self.state_index,
                                  madeline_sprite, (x, y - 1, z), (1, -1, 0), 0.1, 0.4)
            dash = animation_jump(self.screen, self.stage, self.state_index,
                                  madeline_blue_sprite, (x + 1, y - 2, z), (1, 1, 0), 0, 0.2)
            bounce = animation_jump(self.screen, self.stage, self.state_index,
                                    madeline_sprite, (x + 2, y - 1, z), (5, 0, 0), 1, 1)
            anim = chained_animation(self.screen, [jump, dash, bounce], prevent_logic=True, persistent=True)

            self.stage.animation_manager.register_animation(anim)

            g.save_state.hard_save("madeline_present", False)

            self.stage.animation_manager.register_message(self.screen, "Madeline wavedashes away.", 5 * v.FRAME_RATE)

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)
            if g.save_state.get("madeline_present", True):
                x, y = pos
                madeline_sprite = s.sprites["decoration_1x1_madeline"][where_is_player]
                self.screen.blit(madeline_sprite, (x, y-v.BLOCK_Y_SIZE))
