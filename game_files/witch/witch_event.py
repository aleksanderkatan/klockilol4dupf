from game_files.imports.save_state import global_save_state
# where - ((level_set, level), (x, y, z))

class witch_event:
    def __init__(self, where=None, messages=None, index=None):
        if messages is None:
            messages = []
        self.where = where
        self.messages = messages
        self.index = None
        self.current_message_index = None

    def activate(self):
        self.current_message_index = 0

    def current_message(self):
        return self.messages[self.current_message_index]

    def advance(self):
        self.current_message_index += 1
        if len(self.messages) <= self.current_message_index:
            self.current_message_index = None
            global_save_state.complete_event(self.index)
            return None
        return self

    def is_active(self):
        return self.current_message_index is not None
