import src.imports.globals as g
from src.speedruns.speedrun import speedrun


class speedrun_shrek(speedrun):
    def get_starting_stage_and_pos(self):
        return (400, 1), (5, 4, 0)

    def is_condition_met(self):
        return g.save_state.get("shrek", False)

    def get_name(self):
        return "Shrek%"
