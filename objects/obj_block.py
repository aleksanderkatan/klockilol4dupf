import abc
import import_sprites as s

class block(metaclass=abc.ABCMeta):
    def on_step_in(self):
        pass

    def on_step_out(self):
        pass

    def __init__(self, screen, stage, state_index, pos):
        self.screen = screen
        self.stage = stage
        self.sprite = s.sprites["error"]
        self.state_index = state_index
        self.pos = pos

    def replaced_with(self):
        return None

    def draw(self, pos, where_is_player):
        if where_is_player is not None:
            self.screen.blit(self.sprite[where_is_player], pos)

    @abc.abstractmethod
    def copy(self, new_state_index): #!! copy is only for duplicating states
        pass