import abc

class speedrun(metaclass=abc.ABCMeta):
    def get_starting_stage_and_pos(self):
        pass

    def is_condition_met(self):
        pass

    def get_name(self):
        pass

    def does_death_reset(self):
        pass
