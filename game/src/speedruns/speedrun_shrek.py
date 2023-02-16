from src.speedruns.speedrun import speedrun
from src.imports.save_state import global_save_state


class speedrun_shrek(speedrun):
    def get_starting_stage_and_pos(self):
        return (400, 1), (5, 4, 0)

    def is_condition_met(self):
        return global_save_state.get("shrek", False)

    def get_name(self):
        return "Shrek%"
