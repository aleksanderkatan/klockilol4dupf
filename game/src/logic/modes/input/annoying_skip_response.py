from enum import Enum

from src.strings.translation_getters import get_message_strings
import src.imports.globals as g


def edit_distance(s1, s2):
    l1, l2 = len(s1), len(s2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    for i in range(l1 + 1):
        dp[i][0] = i
    for j in range(l2 + 1):
        dp[0][j] = j

    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            subs_cost = 0 if s1[i-1] == s2[j-1] else 1

            dp[i][j] = min(
                dp[i-1][j] + 1,             # del
                dp[i][j-1] + 1,             # insert
                dp[i-1][j-1] + subs_cost    # subs
            )

    return dp[l1][l2]


class status(Enum):
    NOT_SKIP = 0
    INCORRECT_SKIP = 1
    CORRECT_SKIP = 2


def get_annoying_response(expected_string, actual_string):
    if len(actual_string) < 30:
        return None, status.NOT_SKIP

    MS = get_message_strings(g.save_state.get_language())

    if expected_string == actual_string:
        return None, status.CORRECT_SKIP

    if expected_string[:-1] == actual_string:
        return MS.forgot_period, status.INCORRECT_SKIP
    if expected_string.lower() == actual_string.lower():
        return MS.capitalization_matters, status.INCORRECT_SKIP
    if "".join(expected_string.strip().split(" ")) == "".join(actual_string.strip().split(" ")):
        return MS.space_error, status.INCORRECT_SKIP
    dist = edit_distance(expected_string, actual_string)
    if dist == 1 and len(expected_string) == len(actual_string) + 1:
        return MS.to_few_letters, status.INCORRECT_SKIP
    if dist == 1 and len(expected_string) == len(actual_string) - 1:
        return MS.to_much_letters, status.INCORRECT_SKIP
    if dist == 1 and len(expected_string) == len(actual_string):
        return MS.one_wrong_letter, status.INCORRECT_SKIP
    if dist == 2:
        return MS.two_wrong_letters, status.INCORRECT_SKIP
    if dist == 3:
        return MS.three_wrong_letters, status.INCORRECT_SKIP
    if dist <= 10:
        return MS.many_wrong_letters, status.INCORRECT_SKIP


    return None, status.NOT_SKIP


