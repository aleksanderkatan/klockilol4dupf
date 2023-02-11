import abc


class animation(metaclass=abc.ABCMeta):
    def draw(self):
        pass

    def advance(self):
        pass

    def prevents_logic(self):
        pass

    def has_ended(self):
        pass

    def is_persistent(self):  # should it be removed when reversing?
        pass
