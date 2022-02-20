import game_files.imports.all_sprites as s
import game_files.imports.all_blocks as o
from game_files.imports.log import log
from game_files.imports.save_state import global_save_state
from game_files.animations.animation_player_move import animation_player_move
from game_files.animations.animation_player_jump import animation_player_jump
import game_files.imports.globals as g
import game_files.imports.utils as u

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
            self.this_move_direction = direction_suggestion

    def move(self):  # !! set_next_move_direction must be called first
        state = self.stage.states[self.state_index]
        move_length = self.next_move_length
        move_direction = self.this_move_direction

        temp_pos = self.pos
        for i in range(move_length):
            if state.has_barrier(temp_pos, move_direction):
                move_length = i
                break
            temp_pos = u.move_pos(temp_pos, move_direction)

        if move_length == 0:        # moves of length 0 are invalid! (would trigger on_step_out and on_step_in)
            state.invalid = True
            return

        new_pos = u.move_pos(self.pos, move_direction, move_length)
        translation = u.get_translation(self.pos, new_pos)
        if move_length == 1 or move_direction in [4, 5]:
            move_animation = animation_player_move(self.screen, self.stage, self.state_index, translation)
        else:
            move_animation = animation_player_jump(self.screen, self.stage, self.state_index, translation, move_length-1)
        self.stage.animation_manager.register_animation(move_animation)

        if new_pos[2] < 0:
            self.dead = True

        self.next_move_length = 1
        self.last_move_direction = move_direction
        self.last_move_pos = self.pos
        self.this_move_direction = None
        self.pos = new_pos

        if g.CHEATS and g.KBcheat:
            return

        if not self.stage.states[self.state_index].standable(self.pos):
            self.enqueue_move(5)

    def has_something_enqueued(self):
        return self.enqueued_move is not None
