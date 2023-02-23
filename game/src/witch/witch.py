import src.imports.all_sprites as s
import src.imports.globals as g
import src.imports.keybindings as k
from src.witch.witch_box import witch_box


class witch:
    def __init__(self, screen, events):
        self.events = events
        self.screen = screen
        self.active_event = None
        self.text_box = witch_box(self.screen)
        self.last_checked = (None, None)

    def check_for_events(self, level_index, stage):
        if not g.global_save_state.get_preference("witch"):
            return

        if self.active_event is not None:
            return

        if self.last_checked == (level_index, stage.get_player_index()):
            return
            # no need to search through this once again
        self.last_checked = (level_index, stage.get_player_index())

        for event in self.events:
            if g.global_save_state.is_event_completed(event.index):
                continue
            if event.where[0] == level_index and (event.where[1] is None or event.where[1] == stage.get_player_index()):
                self.active_event = event
                event.activate()
                self.update_text_box()
                return

    def draw(self):
        self.screen.blit(s.sprites["background_black"], (0, 0))
        self.screen.blit(s.sprites["witch"], (0, 0))
        self.text_box.draw()

    def update_text_box(self):
        if self.current_message() is not None:
            self.text_box.set_text(self.current_message())

    def handle_key_pressed(self, key):
        if k.is_witch_continue(key):
            if self.active_event is not None:
                self.active_event = self.active_event.advance()
        if k.is_reverse(key):
            if self.active_event is not None:
                self.active_event = self.active_event.reverse()
        self.update_text_box()

    def current_message(self):
        if self.active_event is not None:
            return self.active_event.current_message()
        return None

    def is_active(self):
        return self.active_event is not None
