from resources.strings.english.controls_display import controls_display_en
from resources.strings.english.level_names import level_names_en
from resources.strings.english.messages import messages_en
from resources.strings.english.other import other_en
from resources.strings.polish.controls_display import controls_display_pl
from resources.strings.polish.level_names import level_names_pl
from resources.strings.polish.messages import messages_pl
from resources.strings.polish.other import other_pl


def get_control_display_strings(language):
    match language.lower():
        case "polish":
            return controls_display_pl
        case "english":
            return controls_display_en
    raise RuntimeError(f"Invalid language \"{language}\"")


def get_message_strings(language):
    match language.lower():
        case "polish":
            return messages_pl
        case "english":
            return messages_en
    raise RuntimeError(f"Invalid language \"{language}\"")


def get_level_names_strings(language):
    match language.lower():
        case "polish":
            return level_names_pl
        case "english":
            return level_names_en
    raise RuntimeError(f"Invalid language \"{language}\"")


def get_other_strings(language):
    match language.lower():
        case "polish":
            return other_pl
        case "english":
            return other_en
    raise RuntimeError(f"Invalid language \"{language}\"")

