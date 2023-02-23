import src.imports.utils as u
from src.animations.animation import animation
from src.imports.view_constants import global_view_constants as v


class animation_player_move(animation):
    def __init__(self, screen, stage, state_index, translation):
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

        for i in range(v.MOVE_ANIMATION_LENGTH):
            self.positions.append(
                (SX + (EX - SX) / v.MOVE_ANIMATION_LENGTH * i, SY + (EY - SY) / v.MOVE_ANIMATION_LENGTH * i))

        self.frame = 0
        self.player.ignore_draw = True

    def draw(self):
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
