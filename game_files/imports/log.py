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

class log_class:
    def __init__(self):
        self.i = g.LOG_INFO
        self.w = g.LOG_WARNINGS
        self.e = g.LOG_ERRORS

    def _write(self, log_type, args):
        message = ""
        for arg in args:
            message = message + str(arg) + " "

        if log_type == "INFO":
            print("INFO:", message)
        elif log_type == "WARNING":
            print(colors.WARNING + "WARNING: " + message + colors.ENDC)
        elif log_type == "ERROR":
            print(colors.ERROR + "ERROR: " + message + colors.ENDC)
        elif log_type == "PRINT":
            print(message)

    def info(self, *args):
        if self.i:
            self._write("INFO", args)

    def warning(self, *args):
        if self.w:
            self._write("WARNING", args)

    def error(self, *args):
        if self.e:
            self._write("ERROR", args)

    def print(self, *args):
        self._write("PRINT", args)


log = log_class()
