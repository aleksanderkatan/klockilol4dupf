from game_files.animations.animation import animation
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v
import game_files.imports.utils as u


class animation_player_jump(animation):
    def __init__(self, screen, stage, state_index, translation, height):
        self.screen = screen
        self.stage = stage
        self.state = stage.states[state_index]
        self.player = self.state.player
        self.positions = []
        sx, sy, sz = self.player.pos
        ex, ey, ez = sx + translation[0], sy + translation[1], sz + translation[2]
        tx, ty, tz = self.state.x, self.state.y, self.state.z
        SX, SY = u.index_to_position(sx, sy, sz, tx, ty, tz)
        EX, EY = u.index_to_position(ex, ey, ez, tx, ty, tz)

        # firstly make both go linearly
        for i in range(g.JUMP_ANIMATION_LENGTH):
            self.positions.append(
                (SX + (EX - SX) / g.JUMP_ANIMATION_LENGTH * i, SY + (EY - SY) / g.JUMP_ANIMATION_LENGTH * i))

        # then, add a quadratic function to ys
        F = g.JUMP_ANIMATION_LENGTH
        B = v.BLOCK_Y_SIZE
        for i in range(g.JUMP_ANIMATION_LENGTH):
            x, y = self.positions[i]
            self.positions[i] = x, y - (-4 * height * B / F / F * (i ** 2) + 4 * height * B / F * i + 0)

        self.frame = 0
        self.player.ignore_draw = True

    def draw(self):
        # log.print(f"animation {self.frame}")
        self.screen.blit(self.player.get_current_sprite()[0], self.positions[min(self.frame, len(self.positions))])

    def advance(self):
        self.frame += 1
        self.player.ignore_draw = not self.has_ended()

    def prevents_logic(self):
        return True

    def has_ended(self):
        return self.frame >= len(self.positions)

    def is_persistent(self):
        return False
