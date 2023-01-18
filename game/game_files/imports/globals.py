VERSION = "v0.101"

FRAME_RATE = 30
MOVE_LIMIT = 2048

JUMP_ANIMATION_LENGTH = FRAME_RATE // 2
MOVE_ANIMATION_LENGTH = FRAME_RATE // 15
DISAPPEAR_ANIMATION_LENGTH = FRAME_RATE // 8

VISIBLE_LAYERS_DOWN = 3
VISIBLE_LAYERS_UP = 2
INVISIBLE_BLOCK_0_VISIBILITY = 0.00
INVISIBLE_BLOCK_1_VISIBILITY = 0.02
GRAYNESS = 0.2
THUNDER_PARTICLES = 16
AUTO_SAVE_INTERVAL = 60  # in seconds
FONT_RATIO = 0.59  # width to height for mono, sadly isn't 0.5

MAX_COMMAND_LENGTH = 32
PASSWORD_HASH = b'\xd1\xa0\xd9\x07v\xc0\xd4\x1f\x8f@\xb4\t{\x10\xdf[\xf8;\r\n\x7fx=jO\x01\x97T3_\xefK'

WITCH = True
AUTO_REVERSE = True
TIMER = True
THREED = False  # !! does not quite work

CHEATS = True
FAST_LEVEL_SKIP = True
FAST_LEVEL_SWAP = True

LOG_TRACE = False
LOG_INFO = True
LOG_WARNINGS = True
LOG_ERRORS = True

# runtime variables, don't change
KBcheat = False
PAPOR = False
LAST_ERROR = None
