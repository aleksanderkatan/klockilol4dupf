

class new_save_data:
    def __init__(self, name, language, auto_reverse, timer, skip_witch):
        self.name = name
        self.language = language
        self.auto_reverse = auto_reverse
        self.timer = timer
        self.skip_witch = skip_witch

    def __str__(self):
        return f"new_save_data({self.name}, {self.language}, {self.auto_reverse}, {self.timer}, {self.skip_witch})"
