import src.imports.globals as g
from src.speedruns.speedrun import speedrun
import src.imports.levels as l


class speedrun_test(speedrun):
    def get_starting_stage_and_pos(self):
        return (1, 1), (0, 0, 0)

    def is_condition_met(self):
        for i in range(1, 3+1):
            status = g.save_state.get_level_status((1, i))
            if status != l.level_status.COMPLETED:
                return False
        return True

    def get_name(self):
        return "Test"
