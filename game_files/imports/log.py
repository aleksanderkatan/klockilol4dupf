import game_files.imports.globals as g

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def _write(log_type, args):
    message = ""
    for arg in args:
        message = message + str(arg) + " "

    if log_type == "INFO":
        message = "INFO: " + message
    elif log_type == "WARNING":
        message = colors.WARNING + "WARNING: " + message + colors.ENDC
    elif log_type == "ERROR":
        message = colors.ERROR + "ERROR: " + message + colors.ENDC
    print(message)


class log_class:
    def __init__(self):
        self.i = g.LOG_INFO
        self.w = g.LOG_WARNINGS
        self.e = g.LOG_ERRORS

    def info(self, *args):
        if self.i:
            _write("INFO", args)

    def warning(self, *args):
        if self.w:
            _write("WARNING", args)

    def error(self, *args):
        if self.e:
            _write("ERROR", args)

    def print(self, *args):
        _write("PRINT", args)


log = log_class()
