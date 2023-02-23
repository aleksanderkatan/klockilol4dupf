import src.imports.globals as g



# where - ((level_set, level), (x, y, z))

class witch_event:
    def __init__(self, where=None, messages=None, index=None):
        if messages is None:
            messages = []
        self.where = where
        self.messages = messages
        self.index = index
        self.current_message_index = None

    def activate(self):
        self.current_message_index = 0

    def current_message(self):
        return self.messages[self.current_message_index]

    def advance(self):
        self.current_message_index += 1
        if len(self.messages) <= self.current_message_index:
            self.current_message_index = None
            g.global_save_state.complete_event(self.index)
            return None
        return self

    def reverse(self):
        self.current_message_index = max(0, self.current_message_index-1)
        return self

    def is_active(self):
        return self.current_message_index is not None
