VERSION = "v1.2"

MOVE_LIMIT = 2048

PASSWORD_HASH = b'\xd1\xa0\xd9\x07v\xc0\xd4\x1f\x8f@\xb4\t{\x10\xdf[\xf8;\r\n\x7fx=jO\x01\x97T3_\xefK'
MAX_COMMAND_LENGTH = 60
AUTO_SAVE_INTERVAL = 60  # in seconds

THREED = False  # !! does not quite work

LOG_TRACE = False
LOG_INFO = True
LOG_WARNINGS = True
LOG_ERRORS = True

# this is here because it is also used to make passwords go ****
ENABLE_CHEATS_COMMANDS = ["enable_cheats", "ec"]

# runtime variables, don't change
save_state = None
KBcheat = False
PAPOR = False
LAST_ERROR = None
