import pygame

import source_code.imports.all_sprites as s
import source_code.imports.globals as g
import source_code.imports.utils as u
from source_code.animations.animation_player_jump import animation_player_jump
from source_code.imports.view_constants import global_view_constants as v
from source_code.logic.direction import direction as d

FONT_SIZE_4 = v.LEVEL_FONT_SIZE // 4
FONT = pygame.font.Font(v.FONT_PATH, FONT_SIZE_4)


def _bound_position(pos):
    x_diff = v.BLOCK_X_SIZE//2
    y_diff = v.BLOCK_Y_SIZE//2

    center_x, center_y = pos[0]+x_diff, pos[1]+y_diff
    if center_x <= 0 - x_diff:
        center_x = 2*x_diff
    if v.WINDOW_X + x_diff <= center_x:
        center_x = v.WINDOW_X - 2*x_diff
    if center_y <= 0 - y_diff:
        center_y = 2*y_diff
    if v.WINDOW_Y + y_diff <= center_y:
        center_y = v.WINDOW_Y - 2*y_diff

    return center_x - x_diff, center_y - y_diff


def _triangle_to_draw(pos, bound_position):
    if bound_position == pos:
        return None
    # sorry, I don't see an easier way than 4 cases
    # there definitely is one with like rotation matrices, but this is not complicated enough for me to care
    x_diff = v.BLOCK_X_SIZE//2
    y_diff = v.BLOCK_Y_SIZE//2
    x, y = bound_position
    if pos[0] < bound_position[0]:
        return (x, y), (x, y+2*y_diff), (x-x_diff, y+y_diff)
    if bound_position[0] < pos[0]:
        return (x+2*x_diff, y), (x+2*x_diff, y+2*y_diff), (x+3*x_diff, y+y_diff)
    if pos[1] < bound_position[1]:
        return (x, y), (x+2*x_diff, y), (x+x_diff, y-y_diff)
    if bound_position[1] < pos[1]:
        return (x, y+2*y_diff), (x+2*x_diff, y+2*y_diff), (x+x_diff, y+3*y_diff)




class player:
    def __init__(self, pos, screen, stage, state_index):
        self.pos = pos
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.last_move_direction = d.NONE
        self.this_move_direction = d.NONE
        self.dead = False
        self.enqueued_move = d.NONE
        self.next_move_length = 1
        self.flavour = 0  # 1 - orange, -1 - lemon
        self.last_move_pos = None
        self.ignore_draw = False
        self.flight = -1
        self.switched_controls = False
        self.retain_direction = False

    def get_current_sprite(self):
        if self.flavour in [-1, 1]:
            if self.flavour == 1:
                return s.sprites["flavour_orange"]
            else:
                return s.sprites["flavour_lemon"]
        if g.save_state.get_preference("shrek"):
            return s.sprites["player_shrek"]
        return s.sprites["player"]

    def draw(self, screen_pos):
        if self.ignore_draw:
            return
        bound_pos = _bound_position(screen_pos)
        if bound_pos == screen_pos:
            # inside the screen
            self.screen.blit(self.get_current_sprite()[0], screen_pos)
        else:
            # outside the screen
            triangle = _triangle_to_draw(screen_pos, bound_pos)
            self.screen.blit(self.get_current_sprite()[0], bound_pos)
            pygame.draw.polygon(self.screen, (0, 0, 0), triangle)
        if self.flight >= 0:
            text = f"free moves: {self.flight}"
            txt_surface = FONT.render(text, True, pygame.Color('black'))
            x, y = screen_pos
            self.screen.blit(txt_surface, (x - FONT.size(text)[0] / 2 + v.BLOCK_X_SIZE / 2, y - FONT_SIZE_4 * 1.5))

    def copy(self, new_state_index):
        pla = player(self.pos, self.screen, self.stage, new_state_index)
        pla.last_move_direction = self.last_move_direction
        pla.this_move_direction = self.this_move_direction
        pla.dead = self.dead
        pla.enqueued_move = self.enqueued_move
        pla.next_move_length = self.next_move_length
        pla.last_move_pos = self.last_move_pos
        pla.flavour = self.flavour
        pla.ignore_draw = self.ignore_draw
        pla.flight = self.flight
        pla.switched_controls = self.switched_controls
        pla.retain_direction = self.retain_direction
        return pla

    def retain_direction_after_next_jump(self):
        self.retain_direction = True

    def enqueue_move(self, direction):
        self.enqueued_move = direction

    def boost_next_move(self, amount):
        self.next_move_length = amount

    def set_next_move_direction(self, direction_suggestion):
        if self.enqueued_move != d.NONE:
            direction = self.enqueued_move
            self.this_move_direction = direction
            self.enqueued_move = d.NONE
        else:
            if self.switched_controls:
                if u.reverse_direction(direction_suggestion) != d.NONE:
                    direction_suggestion = u.reverse_direction(direction_suggestion)
            self.this_move_direction = direction_suggestion

    def move(self):  # !! set_next_move_direction must be called first
        state = self.stage.states[self.state_index]
        move_length = self.next_move_length
        move_direction = self.this_move_direction

        # moves longer than 1 are considered to be jumps and therefore surpass barriers
        if move_length == 1:
            if state.has_barrier(self.pos, move_direction):
                state.invalid = True
                return

        new_pos = u.move_pos(self.pos, move_direction, move_length)
        translation = u.get_translation(self.pos, new_pos)

        if move_length != 1 and move_direction.is_cardinal():
            move_animation = animation_player_jump(self.screen, self.stage, self.state_index, translation,
                                                   (move_length - 1) / 2, move_length / 4)
            self.stage.animation_manager.register_animation(move_animation)
        if move_direction == d.DESCEND:
            move_animation = animation_player_jump(self.screen, self.stage, self.state_index, (0, 0, -move_length),
                                                   0, 0.15 * move_length)
            self.stage.animation_manager.register_animation(move_animation)
        # if move_direction == d.ASCEND:
        #     move_animation = animation_player_jump(self.screen, self.stage, self.state_index, (0, 0, move_length),
        #                                            0, 0.15 * move_length)
        #     self.stage.animation_manager.register_animation(move_animation)

        if new_pos[2] < 0:
            self.dead = True

        self.next_move_length = 1
        if move_length > 1:  #
            if self.retain_direction:
                self.retain_direction = False
                self.last_move_direction = move_direction
            else:
                self.last_move_direction = d.NONE
        else:
            self.last_move_direction = move_direction

        self.last_move_pos = self.pos
        self.this_move_direction = d.NONE
        self.pos = new_pos

        if g.KBcheat and g.save_state.get_preference("cheats"):
            return

        if not self.stage.states[self.state_index].standable(self.pos) and self.flight <= 0:
            self.enqueue_move(d.DESCEND)
        self.flight -= 1

    def has_something_enqueued(self):
        return self.enqueued_move != d.NONE
