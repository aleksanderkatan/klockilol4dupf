import source_code.imports.globals as g
from source_code.speedruns.speedrun import speedrun


class speedrun_perfectionist(speedrun):
    def get_starting_stage_and_pos(self):
        return (400, 1), (5, 4, 0)

    def is_condition_met(self):
        return g.save_state.get_completion(True) == 1

    def get_name(self):
        return "100%"
