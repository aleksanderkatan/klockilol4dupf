import src.imports.globals as g


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


def _write_colored(log_type, args):
    message = ""
    for arg in args:
        message = message + str(arg) + " "

    if log_type == "TRACE":
        message = colors.OKCYAN + "TRACE: " + message + colors.ENDC
    elif log_type == "INFO":
        message = "INFO: " + message
    elif log_type == "WARNING":
        message = colors.WARNING + "WARNING: " + message + colors.ENDC
    elif log_type == "ERROR":
        message = colors.ERROR + "ERROR: " + message + colors.ENDC
    elif log_type == "WRITE":
        # message = "WRITE: " + message
        pass
    print(message)


class log_class:
    def __init__(self):
        self.t = g.LOG_TRACE
        self.i = g.LOG_INFO
        self.w = g.LOG_WARNINGS
        self.e = g.LOG_ERRORS

    def trace(self, *args):
        if self.t:
            _write_colored("TRACE", args)

    def info(self, *args):
        if self.i:
            _write_colored("INFO", args)

    def warning(self, *args):
        if self.w:
            _write_colored("WARNING", args)

    def error(self, *args):
        if self.e:
            _write_colored("ERROR", args)

    def write(self, *args):
        _write_colored("WRITE", args)


log = log_class()
