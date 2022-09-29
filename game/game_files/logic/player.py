import game_files.imports.all_sprites as s
from game_files.imports.save_state import global_save_state
from game_files.animations.animation_player_jump import animation_player_jump
import game_files.imports.globals as g
from game_files.imports.view_constants import global_view_constants as v
import game_files.imports.utils as u
import pygame

FONT_SIZE_4 = v.LEVEL_FONT_SIZE//4
FONT = pygame.font.Font("game_files/fonts/mono/ttf/JetBrainsMono-Regular.ttf", FONT_SIZE_4)

class player:
    def __init__(self, pos, screen, stage, state_index):
        self.pos = pos
        self.screen = screen
        self.stage = stage
        self.state_index = state_index
        self.last_move_direction = None
        self.this_move_direction = None
        self.dead = False
        self.enqueued_move = None
        self.next_move_length = 1
        self.flavour = 0    # 1 - orange, -1 - lemon
        self.last_move_pos = None
        self.ignore_draw = False
        self.flight = -1
        self.switched_controls = False

    def get_current_sprite(self):
        if self.flavour in [-1, 1]:
            if self.flavour == 1:
                return s.sprites["flavour_orange"]
            else:
                return s.sprites["flavour_lemon"]
        if global_save_state.get("shrek", False):
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
            self.screen.blit(txt_surface, (x-FONT.size(text)[0]/2+v.BLOCK_X_SIZE/2, y-FONT_SIZE_4*1.5))

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
        return pla

    def enqueue_move(self, direction):
        self.enqueued_move = direction

    def boost_next_move(self, amount):
        self.next_move_length = amount

    def set_next_move_direction(self, direction_suggestion):
        if self.enqueued_move is not None:
            direction = self.enqueued_move
            self.this_move_direction = direction
            self.enqueued_move = None
        else:
            if self.switched_controls:
                if u.reverse_direction(direction_suggestion) is not None:
                    direction_suggestion = u.reverse_direction(direction_suggestion)
            self.this_move_direction = direction_suggestion

    def move(self):  # !! set_next_move_direction must be called first
        state = self.stage.states[self.state_index]
        move_length = self.next_move_length
        move_direction = self.this_move_direction

        # direction:
        # 0 - right
        # 1 - up
        # 2 - left
        # 3 - down
        # 4 - rise
        # 5 - fall
        # 6 - forced no move (eg. there is a piston pusher moving)
        # None - player did not input anything

        # moves longer than 1 are considered jumps and therefore surpass barriers
        if move_length == 1:
            if state.has_barrier(self.pos, move_direction):
                state.invalid = True
                return

        new_pos = u.move_pos(self.pos, move_direction, move_length)
        translation = u.get_translation(self.pos, new_pos)

        move_animation = None
        if self.stage.level_index[0] == 209 and (move_length == 1 or move_direction in [4, 5]):     # animate only in PM zone... or not
            pass
            # move_animation = animation_player_move(self.screen, self.stage, self.state_index, translation)
        elif move_length != 1 and move_direction in [0, 1, 2, 3]:
            move_animation = animation_player_jump(self.screen, self.stage, self.state_index, translation, (move_length-1)/2)

        if move_animation is not None:
            self.stage.animation_manager.register_animation(move_animation)

        if new_pos[2] < 0:
            self.dead = True

        self.next_move_length = 1
        self.last_move_direction = None if move_length > 1 else move_direction
        self.last_move_pos = self.pos
        self.this_move_direction = None
        self.pos = new_pos

        if g.CHEATS and g.KBcheat:
            return

        if not self.stage.states[self.state_index].standable(self.pos) and self.flight <= 0:
            self.enqueue_move(5)
        self.flight -= 1

    def has_something_enqueued(self):
        return self.enqueued_move is not None
