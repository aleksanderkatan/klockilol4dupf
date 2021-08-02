import pygame as pg
import game_files.imports.all_sprites as s
import game_files.imports.globals as g
import game_files.imports.keybindings as k
from game_files.witch.witch_box import witch_box
from game_files.witch.events import events
from game_files.imports.save_state import global_save_state

class witch:
    def __init__(self, screen):
        self.events = events
        self.screen = screen
        self.active_event = None
        self.text_box = witch_box(self.screen)

    def check_for_events(self, level_index, stage):
        if g.WITCH is False:
            return

        if self.active_event is not None:
            return

        for event in self.events:
            if global_save_state.is_event_completed(event.index):
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
        self.update_text_box()

    def current_message(self):
        if self.active_event is not None:
            return self.active_event.current_message()
        return None

    def is_active(self):
        return self.active_event is not None
