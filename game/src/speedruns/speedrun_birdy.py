import src.imports.globals as g
from src.speedruns.speedrun import speedrun
import src.imports.levels as l


class speedrun_birdy(speedrun):
    def get_starting_stage_and_pos(self):
        return (205, 1), (6, 0, 0)

    def is_condition_met(self):
        return g.save_state.get_set_status(205) == l.level_status.COMPLETED

    def get_name(self):
        return "Birdy's Rainy Day Skipathon"
