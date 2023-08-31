from src.strings.english.controls_display import controls_display_en
from src.strings.polish.controls_display import controls_display_pl



def get_control_display_strings(language):
    match language.lower():
        case "polish":
            return controls_display_pl
        case "english":
            return controls_display_en
    raise RuntimeError(f"Invalid language \"{language}\"")




