import src.imports.all_sprites as s
import src.imports.globals as g
from src.blocks.block import block
from src.imports.log import log


class block_shrek(block):
    def __init__(self, screen, stage, state_index, pos):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block"]
        self.player_sprite = {True: s.sprites["player"][0], False: s.sprites["player_shrek"][0]}

    def copy(self, new_state_index):
        return block_shrek(self.screen, self.stage, new_state_index, self.pos)

    def on_step_in(self):
        g.save_state.set_preference("shrek", not g.save_state.get_preference("shrek"))
        self.stage.speedrun_check_needed = True
        log.write(g.save_state.get_all_stats())

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)
            self.screen.blit(self.player_sprite[g.save_state.get_preference("shrek")], pos)
