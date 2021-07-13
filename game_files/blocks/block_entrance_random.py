from game_files.blocks.block import block
import game_files.imports.all_sprites as s
from game_files.imports.log import log
from game_files.level_generators.less_simple_level_generator import generate


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
        if self.configuration not in [1, 2]:
            log.error("Random entrance configuration invalid")
            self.target_level = None
            return

        if self.configuration == 1:
            self.target_level = (101, 0)
        elif self.configuration == 2:
            self.target_level = (102, 0)

    def on_step_in(self):
        if self.configuration == 1:
            generate(index=self.target_level, x=9, y=9, ice=0, jump2=0, jump3=0, arrow=0, length=60, redirect=6, max_num=4,
                     min_total=30)
        elif self.configuration == 2:
            # generate(index=self.target_level, x=11, y=11, ice=10, jump2=6, jump3=6, arrow=12, length=60, redirect=5, max_num=3,
            #          min_total=30)
            generate(index=self.target_level, x=6, y=6, ice=0, jump2=15, jump3=0, arrow=0, length=20, redirect=3, max_num=3,
                     min_total=None)

        self.stage.change_to = self.target_level

    def on_step_out(self):
        self.stage.change_to = None

    def get_target_level(self):
        return self.target_level


