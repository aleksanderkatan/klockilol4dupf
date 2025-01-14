import source_code.imports.all_random_level_generators as r
import source_code.imports.all_sprites as s
from source_code.blocks.block import block
from source_code.imports.log import log


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
        if self.configuration not in [1, 2, 3, 4]:
            log.error("Random entrance configuration invalid.")
            self.target_level = None
            return

        self.target_level = (100 + self.configuration, 0)

    def on_step_in(self):
        # also add above!
        result = False
        match self.configuration:
            case 1:
                result = r.generate_LSLG(index=self.target_level, x=8, y=8, ice=0, jump2=0, jump3=0, arrow=0, length=50,
                                         redirect=5, max_num=3, min_total=30)
            case 2:
                result = r.generate_LSLG(index=self.target_level, x=8, y=8, ice=0, jump2=10, jump3=0, arrow=0,
                                         length=50,
                                         redirect=3, max_num=3, min_total=None)
            case 3:
                result = r.generate_PLG(index=self.target_level, x=7, y=7, portals=4, min_portals=2, pair_portals=True,
                                        length=30, redirect=4)
            case 4:
                result = r.generate_EULG()

        if result is None or not result:
            return
        self.stage.change_to = self.target_level

    def on_step_out(self):
        self.stage.change_to = None

    def get_target_level(self):
        return self.target_level
