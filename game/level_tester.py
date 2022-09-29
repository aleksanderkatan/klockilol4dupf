import pygame
import random
import time
pygame.init()
tested_level = (207, 5)
max_moves = 34
# YES, it has to show the screen. I wanted it to show the character moving rapidly but I failed.
screen = pygame.display.set_mode((100, 100))
pygame.display.set_caption('level_tester')
import game_files.imports.globals as g
g.LOG_INFO = False
from game_files.logic.stage import stage
s = stage(screen, tested_level, (0, 0))
moves = []

def test():
    if len(moves) > max_moves:
        return False

    this_move = [0, 1, 2, 3]
    random.shuffle(this_move)
    for mov in this_move:
        moves.append(mov)
        s.move(mov)
        # s.draw()
        # time.sleep(1)
        while s.latest_state().is_next_move_forced() and not s.latest_state().player.dead and not s.latest_state().completed:
            s.move()

        if s.latest_state().completed:
            return True

        if not s.latest_state().player.dead:
            res = test()
            if res is True:
                return True
        s.reverse()
        moves.pop(-1)
    return False


def count():
    total = 0
    this_move = [0, 1, 2, 3]
    random.shuffle(this_move)
    for mov in this_move:
        moves.append(mov)
        s.move(mov)
        while s.latest_state().is_next_move_forced() and not s.latest_state().player.dead and not s.latest_state().completed:
            s.move()

        if s.latest_state().completed:
            return 1

        if not s.latest_state().player.dead:
            total += count()
        s.reverse()
        moves.pop(-1)
    return total


# test()
# ans = str(moves)
# ans = ans.replace(", ", "")
# ans = ans.replace("[", "")
# ans = ans.replace("]", "")
# ans = ans.replace("0", ">")
# ans = ans.replace("1", "^")
# ans = ans.replace("2", "<")
# ans = ans.replace("3", "v")
# print(ans)
print(count())

