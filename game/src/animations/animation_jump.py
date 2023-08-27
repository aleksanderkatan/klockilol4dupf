import src.imports.utils as u
from src.animations.animation import animation
from src.imports.view_constants import global_view_constants as v


class animation_jump(animation):
    def __init__(self, screen, stage, state_index,
                 sprite, start_pos, translation, height, duration,
                 prevent_logic=False, persistent=False):
        self.screen = screen
        self.stage = stage


        self.positions = []
        sx, sy, sz = start_pos
        ex, ey, ez = sx + translation[0], sy + translation[1], sz + translation[2]
        state = stage.states[state_index]
        tx, ty, tz = state.x, state.y, state.z
        SX, SY = u.index_to_position(sx, sy, sz, tx, ty, tz)
        EX, EY = u.index_to_position(ex, ey, ez, tx, ty, tz)

        # firstly make both go linearly
        total_frames = int(duration * v.FRAME_RATE)
        for i in range(total_frames):
            self.positions.append(
                (SX + (EX - SX) / total_frames * i, SY + (EY - SY) / total_frames * i))

        # then, add a quadratic function to ys
        F = total_frames
        B = v.BLOCK_Y_SIZE
        for i in range(total_frames):
            x, y = self.positions[i]
            self.positions[i] = x, y - (-4 * height * B / F / F * (i ** 2) + 4 * height * B / F * i + 0)

        self.frame = 0
        self.sprite = sprite
        self.prevent_logic = prevent_logic
        self.persistent = persistent

    def draw(self):
        index = min(self.frame, len(self.positions)-1)
        pos = self.positions[index]
        self.screen.blit(self.sprite, pos)

    def advance(self):
        self.frame += 1

    def prevents_logic(self):
        return self.prevent_logic

    def has_ended(self):
        return self.frame >= len(self.positions)

    def is_persistent(self):
        return self.persistent
