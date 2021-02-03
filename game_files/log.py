import game_files.globals as g

class log_class:
    def __init__(self):
        self.i = g.LOG_INFO
        self.w = g.LOG_WARNINGS
        self.e = g.LOG_ERRORS

    def info(self, message):
        if self.i:
            print("INFO:", message)

    def warning(self, message):
        if self.w:
            print("WARNING:", message)

    def error(self, message):
        if self.e:
            print("ERROR:", message)


log = log_class()
