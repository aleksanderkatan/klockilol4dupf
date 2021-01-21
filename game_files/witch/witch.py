from game_files.witch.events import events
from game_files.save_state import global_save_state
import pygame as pg
import game_files.all_sprites as s
from game_files.witch.witch_box import witch_box
import game_files.config as c

class witch:
    def __init__(self, screen):
        self.events = events
        self.screen = screen
        self.active_event = None
        self.text_box = witch_box(self.screen)

    def check_for_events(self, level_index, stage):
        if c.WITCH is False:
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
        self.screen.blit(s.sprites["black"], (0, 0))
        self.screen.blit(s.sprites["witch"], (0, 0))
        self.text_box.draw()

    def update_text_box(self):
        if self.current_message() is not None:
            self.text_box.set_text(self.current_message())

    def handle_event(self, event):
        if event.key == pg.K_SPACE:
            if self.active_event is not None:
                self.active_event = self.active_event.advance()
        self.update_text_box()

    def current_message(self):
        if self.active_event is not None:
            return self.active_event.current_message()
        return None

    def is_active(self):
        return self.active_event is not None
