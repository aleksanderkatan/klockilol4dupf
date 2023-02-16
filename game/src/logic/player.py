import src.imports.all_sprites as s
from src.imports.save_state import global_save_state
from src.animations.animation_player_jump import animation_player_jump
import src.imports.globals as g
from src.imports.view_constants import global_view_constants as v
import src.imports.utils as u
import pygame
from src.logic.direction import direction as d

FONT_SIZE_4 = v.LEVEL_FONT_SIZE // 4
FONT = pygame.font.Font("src/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_4)


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
        if global_save_state.get_preference("shrek"):
            return s.sprites["player_shrek"]
        return s.sprites["player"]

    def draw(self, screen_pos):
        if self.ignore_draw:
            return
        self.screen.blit(self.get_current_sprite()[0], screen_pos)
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

        # moves longer than 1 are considered jumps and therefore surpass barriers
        if move_length == 1:
            if state.has_barrier(self.pos, move_direction):
                state.invalid = True
                return

        new_pos = u.move_pos(self.pos, move_direction, move_length)
        translation = u.get_translation(self.pos, new_pos)

        if move_length != 1 and move_direction.is_cardinal():
            move_animation = animation_player_jump(self.screen, self.stage, self.state_index, translation,
                                                   (move_length - 1) / 2)
            self.stage.animation_manager.register_animation(move_animation)

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

        if g.KBcheat and global_save_state.get_preference("cheats"):
            return

        if not self.stage.states[self.state_index].standable(self.pos) and self.flight <= 0:
            self.enqueue_move(d.DESCEND)
        self.flight -= 1

    def has_something_enqueued(self):
        return self.enqueued_move != d.NONE
