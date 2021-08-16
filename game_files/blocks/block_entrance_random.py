from game_files.blocks.block import block
import game_files.imports.all_sprites as s
from game_files.imports.log import log
import game_files.imports.all_random_level_generators as r


class block_entrance_random(block):
    def __init__(self, screen, stage, state_index, pos, configuration=1):
        super().__init__(screen, stage, state_index, pos)
        self.sprite = s.sprites["block_entrance_random"]
        self.configuration = configuration
        self.target_level = None
        self.update_target_level()

    def copy(self, new_state_index):
        return block_entrance_random(self.screen, self.stage, new_state_index, self.pos, self.configuration)

    def options(self, option):
        self.configuration = int(option)
        self.update_target_level()

    def update_target_level(self):
        if self.configuration not in [1, 2, 3]:
            log.error("Random entrance configuration invalid")
            self.target_level = None
            return

        if self.configuration == 1:
            self.target_level = (101, 0)
        elif self.configuration == 2:
            self.target_level = (102, 0)
        elif self.configuration == 3:
            self.target_level = (103, 0)

    def on_step_in(self):
        # also add above!
        result = False
        if self.configuration == 1:
            result = r.generate_LSLG(index=self.target_level, x=8, y=8, ice=0, jump2=0, jump3=0, arrow=0, length=50,
                                     redirect=5, max_num=3, min_total=30)
        elif self.configuration == 2:
            # result = r.generate_LSLG(index=self.target_level, x=6, y=6, ice=0, jump2=15, jump3=0, arrow=0, length=20,
            #                          redirect=4, max_num=3, min_total=None)
            result = r.generate_LSLG(index=self.target_level, x=8, y=8, ice=0, jump2=10, jump3=0, arrow=0, length=50,
                                     redirect=3, max_num=3, min_total=None)
        elif self.configuration == 3:
            result = r.generate_PLG(index=self.target_level, x=7, y=7, portals=4, min_portals=2, pair_portals=True, length=30, redirect=4)

        if result is None or not result:
            return
        self.stage.change_to = self.target_level

    def on_step_out(self):
        self.stage.change_to = None

    def get_target_level(self):
        return self.target_level
