from src.imports.view_constants import global_view_constants as v
from src.imports.keybindings import is_held_relevant

INITIAL_COOLDOWN = int(0.3 * v.FRAME_RATE)
REPEAT_COOLDOWN = int(0.1 * v.FRAME_RATE)


class key_repeater:
    def __init__(self):
        self.latest_key_pressed = None
        self.latest_key_unicode = None
        self.initial_cooldown = INITIAL_COOLDOWN
        self.repeat_cooldown = 0

    def register_key_pressed(self, key, unicode):
        self.latest_key_pressed = key
        self.latest_key_unicode = unicode
        self.initial_cooldown = INITIAL_COOLDOWN
        self.repeat_cooldown = 0

    def get_repeated_key(self, keys_pressed):
        if self.latest_key_pressed is None:
            return
        if keys_pressed[self.latest_key_pressed] and is_held_relevant(self.latest_key_pressed):
            return self._held()
        self._released()
        return None

    def _held(self):
        self.initial_cooldown -= 1
        self.repeat_cooldown -= 1
        if self.initial_cooldown <= 0 and self.repeat_cooldown <= 0:
            self.repeat_cooldown = REPEAT_COOLDOWN
            return self.latest_key_pressed, self.latest_key_unicode
        return None

    def _released(self):
        self.latest_key_pressed = None
        self.initial_cooldown = INITIAL_COOLDOWN
        self.repeat_cooldown = 0

