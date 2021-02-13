import game_files.globals as g

class bcolors:
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

    def info(self, message):
        if self.i:
            print("INFO:", message)

    def warning(self, message):
        if self.w:
            print(bcolors.WARNING + "WARNING: " + message + bcolors.ENDC)

    def error(self, message):
        if self.e:
            print(bcolors.ERROR + "ERROR: " + message + bcolors.ENDC)


log = log_class()
