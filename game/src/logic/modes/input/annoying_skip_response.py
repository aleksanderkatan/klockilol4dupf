import editdistance
from enum import Enum

from src.strings.translation_getters import get_message_strings
import src.imports.globals as g


class status(Enum):
    NOT_SKIP = 0
    INCORRECT_SKIP = 1
    CORRECT_SKIP = 2


def get_annoying_response(expected_string, actual_string):
    MS = get_message_strings(g.save_state.get_language())

    if expected_string == actual_string:
        return None, status.CORRECT_SKIP

    if expected_string[:-1] == actual_string:
        return MS.forgot_period, status.INCORRECT_SKIP
    if expected_string.lower() == actual_string.lower():
        return MS.capitalization_matters, status.INCORRECT_SKIP
    if "".join(expected_string.strip().split(" ")) == "".join(actual_string.strip().split(" ")):
        return MS.space_error, status.INCORRECT_SKIP
    edit_distance = editdistance.eval(expected_string, actual_string)
    if edit_distance == 1 and len(expected_string) == len(actual_string) + 1:
        return MS.to_few_letters, status.INCORRECT_SKIP
    if edit_distance == 1 and len(expected_string) == len(actual_string) - 1:
        return MS.to_much_letters, status.INCORRECT_SKIP
    if edit_distance == 1 and len(expected_string) == len(actual_string):
        return MS.one_wrong_letter, status.INCORRECT_SKIP
    if edit_distance == 2:
        return MS.two_wrong_letters, status.INCORRECT_SKIP
    if edit_distance == 3:
        return MS.three_wrong_letters, status.INCORRECT_SKIP
    if edit_distance <= 10:
        return MS.many_wrong_letters, status.INCORRECT_SKIP


    return None, status.NOT_SKIP



